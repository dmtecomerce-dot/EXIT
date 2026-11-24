# EXIT

Privat kontrollrum för EXIT. Innehållet i `data.enc.json` är krypterat och kan bara låsas upp med lösenordet.

- `index.html` – appen (låses upp i webbläsaren)
- `setup.html` – engångssida för att välja lösenord och skapa `keys.json`
- `encrypt.py` – krypterar dagens data med publika nyckeln i `keys.json`
