# 🍽️ TipMaster - Kalkulator Tip Restaurant

Aplikasi Python untuk menghitung tip restaurant dengan fitur split bill.

## ✨ Fitur

- ✅ Hitung tip dengan berbagai persentase (10%, 15%, 20%, atau custom)
- ✅ Split bill untuk beberapa orang
- ✅ Format output Rupiah yang rapi
- ✅ Validasi input yang robust
- ✅ Modular programming untuk kemudahan maintenance

## 📁 Struktur Proyek

```
tipmaster/
├── main.py           # Entry point aplikasi
├── calculator.py     # Logika perhitungan matematika
├── input_handler.py  # Validasi dan handling input user
├── formatter.py      # Format dan display output
└── README.md         # Dokumentasi
```

## 🚀 Cara Menjalankan

1. Pastikan Python 3.6+ terinstall
2. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## 📖 Konsep yang Dipelajari

- Operator aritmatika Python (+, -, *, /, %)
- String formatting dengan f-strings
- Modular programming
- Input validation
- Error handling dengan try-except
- Function organization

## 💡 Contoh Penggunaan

```
==================================================
🍽️  TIPMASTER - KALKULATOR TIP RESTAURANT  🍽️
==================================================
Masukkan total bill (Rp): 150000

Pilih persentase tip:
1. 10%
2. 15%
3. 20%
4. Custom

Pilihan Anda (1-4): 2

Apakah ingin split bill? (y/n): y

Jumlah orang untuk split bill: 3

==================================================
📊 RINCIAN PEMBAYARAN
==================================================
Total Bill        : Rp 150,000.00
Tip (15%)         : Rp 22,500.00
--------------------------------------------------
TOTAL             : Rp 172,500.00
==================================================
Dibagi 3 orang
Per Orang         : Rp 57,500.00
==================================================
```

## 🎓 Pembelajaran

Project ini mendemonstrasikan:
- Pemisahan concerns (separation of concerns)
- Single Responsibility Principle
- Clean code practices
- User experience yang baik dengan validasi input