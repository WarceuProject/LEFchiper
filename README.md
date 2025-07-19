# LEFchiper
Local Encryption Fonetic Chiper

#experimental
# LEFchiper
**Local Encryption Fonetic Chiper**

LEFchiper adalah proyek eksperimental enkripsi lokal yang menggabungkan beberapa metode transformasi fonetik dan algoritma kustom seperti `glasicc`, `lefchaos`, dan lainnya. Dirancang untuk fleksibilitas dan eksplorasi, LEFchiper mendukung multiple mode sekaligus dan dapat dijalankan langsung tanpa instalasi penuh.

> ⚠️ **Project ini bersifat eksperimental** – jangan gunakan untuk keperluan keamanan serius.

---

## 📦 Fitur Utama

- ✨ Multiple encryption mode secara berurutan (chain-mode)
- 🔐 Dukungan penggunaan kunci (`-k`)
- 🧩 Modular (setiap mode disimpan dalam file/module terpisah)
- 🚀 Bisa dijalankan langsung sebagai modul Python

---

## 📁 Contoh Struktur Direktori
```
LEFchiper
.
├── LICENSE
├── README.md
├── lefchiper
│   ├── __init__.py
│   ├── __main__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── __main__.cpython-312.pyc
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── glasicc.cpython-312.pyc
│   │   │   ├── lefchaos.cpython-312.pyc
│   │   │   └── lefkey.cpython-312.pyc
│   │   ├── glasicc.py
│   │   ├── lefchaos.py
│   │   └── lefkey.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── pyproject.toml
└── tests
    ├── __init__.py
    ├── __main__.py
    ├── test_glasicc.py
    ├── test_lefchaos.py
    └── test_lefkey.py

8 directories, 24 files
```

🧪 Jalankan (tanpa instalasi)
```
python3-m lefchiper -e "Halo Dunia" -m glasiccpython3 lefchaos -k 123
```

🧪 Dev Mode
```
pip install -e .
```

Install di Internal 
```
pip install .
```
