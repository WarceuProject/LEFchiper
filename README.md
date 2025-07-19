#experimental
# LEFchiper
**Local Encryption Fonetic Chiper**

LEFchiper adalah proyek eksperimental enkripsi lokal yang menggabungkan beberapa metode transformasi fonetik dan algoritma kustom seperti `glasicc`, `lefchaos`, dan lainnya. Dirancang untuk fleksibilitas dan eksplorasi, LEFchiper mendukung multiple mode sekaligus dan dapat dijalankan langsung tanpa instalasi penuh.
Eksperimen enkripsi lokal ini berbasis fonetik dan pola kekacauan unik.  
Proyek ini terdiri dari beberapa mode enkripsi yang bisa digunakan dengan cepat langsung via command line.

## ✨ Awal Mula

Awal mula proyek ini datang dari kenangan masa kecil, saat saya dan teman-teman berbicara dengan “bahasa aneh” yang sering disebut sebagai **Bahasa G** — contohnya kata "halo" diucapkan sebagai "hagalogo".  
Bahasa ini menginspirasi saya untuk mengembangkan **mode `glasicc`**, yang merupakan implementasi fonetik tersebut ke dalam algoritma sederhana.
Rumus Pola Dasar:
Teks Asli: Halo jadi ```Ha(g+vokal)lo(g+vokal) = ha(ga)lo(go) = hagalogo```

___________________________________
| Input   | Output (Glasicc Mode) |
|---------|-----------------------|
| halo    | hagalogo              |
| dunia   | dugunigiaga           |
| enkripsi| egenkrigipsigi        |

Kode pseudo:
```python
output = ""
for huruf in teks:
    if huruf in vokal:
        output += huruf + "g" + huruf
    else:
        output += huruf
```
Seiring waktu, saya mulai tertarik untuk menggabungkan ide kekacauan, logika obfuscation, serta penyisipan kunci sebagai faktor tambahan. Maka, lahirlah mode-mode lainnya seperti `lefchaos` dan `lefkey`.

LEFchiper adalah gabungan dari:
- `LEF` = Local Encryption Fonetik
- `chiper` = Bentukan kata dari cipher, dengan pelafalan yang khas




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

# 👥 Kontribusi github
Kami membuka pintu untuk kontribusi dari siapa pun yang tertarik mengembangkan metode transformasi teks kreatif. Hubungi komunitas Warceu Project atau buat pull request di GitHub kami.