#!/usr/bin/env python3
"""Krypterar dagens data till data.enc.json med publika nyckeln i keys.json.

Användning: python3 encrypt.py data.json keys.json data.enc.json
Kräver: pip install cryptography
"""
import base64, json, os, sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def b64u_int(s):
    s += "=" * (-len(s) % 4)
    return int.from_bytes(base64.urlsafe_b64decode(s), "big")


def main(src, keys_path, dst):
    with open(src, "rb") as f:
        plain = f.read()
    json.loads(plain)  # måste vara giltig JSON
    with open(keys_path) as f:
        keys = json.load(f)
    pub = rsa.RSAPublicNumbers(b64u_int(keys["pub"]["e"]), b64u_int(keys["pub"]["n"])).public_key()
    aes_key = AESGCM.generate_key(bit_length=256)
    iv = os.urandom(12)
    ct = AESGCM(aes_key).encrypt(iv, plain, None)
    ek = pub.encrypt(aes_key, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    out = {"v": 1, "ek": base64.b64encode(ek).decode(), "iv": base64.b64encode(iv).decode(), "ct": base64.b64encode(ct).decode()}
    with open(dst, "w") as f:
        json.dump(out, f)
    print(f"Krypterade {len(plain)} byte -> {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Användning: encrypt.py data.json keys.json data.enc.json")
    main(*sys.argv[1:])
