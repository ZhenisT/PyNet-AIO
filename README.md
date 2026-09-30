# PyNet-AIO

PyNet - python networking with receipts, LAN-chat, and ESC-POS emulator, made by 11 years-old boy!!!

### 🛒 `main.py` — POS Cashier
* **`[+=]` Money Box** — An infinite loop takes item codes and uses the `+=` operator to accumulate the total price (accumulator).
* **`[EAN8]` Barcode** — Python grabs the current year and glues it together with 4 random digits, creating a clean 8-digit barcode.
* **`[Network]` Shoot** — On `pay` command, the library translates text, barcode, and the `.cut()` command into bytes and shoots them across the TCP socket.

### 🖥️ `emu.py` — Print Server
* **`[Thread]` Background** — Network listening is moved to a background thread on port `9100`, keeping the console unfrozen and always ready to print.
* **`[cp0409]` Retro Vibe** — Catches raw bytes `b""` and decodes them into clean US ASCII text, throwing away messy layout characters.

### 📠 `faxing.py` — PyFax LAN-Chat
* **`[Socket]` Pure Net** — Runs on raw sockets without any printer libraries. Direct computer-to-computer connection.
* **`[ID]` Stamp** — Generates a random `ID fax` for every message, acting as a unique sender signature on the network.
* **`[Stream]` Fax Print** — Encodes the message into bytes and sends it to the emulator, which prints lines one by one with a delay, mimicking real Brother 2001 thermal paper.

***
🔒 **`PyFax - copyright 2026 PyNet (11 years boy) RUSTECH`**
