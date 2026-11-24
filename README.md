# EXIT

Privat kontrollrum för EXIT. Innehållet i `data.enc.json` är krypterat och kan bara låsas upp med lösenordet.

- `index.html` – appen (låses upp i webbläsaren)
- `setup.html` – engångssida för att välja lösenord och skapa `keys.json`
- `encrypt.py` – krypterar dagens data med publika nyckeln i `keys.json`

## Nattschema

| Tid | Bot |
|---|---|
| 03:13 | Butiksspåraren – nya butiker via org.nr |
| 04:00 | Konkurrentbevakaren – nya produkter och räckvidd |
| 04:41 | Produktjägaren – vinnare utomlands |
| 05:47 | Morgonuppdatering – krypterar och publicerar `data.enc.json` |
