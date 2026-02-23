"""
Module: constants.py
Deskripsi: Menyimpan semua konstanta yang digunakan dalam aplikasi konverter suhu
Best Practice: Pisahkan konstanta dalam file terpisah untuk maintainability
"""

# Konstanta untuk rumus konversi suhu
# Menggunakan UPPER_CASE untuk konstanta (PEP 8 convention)

# Titik beku absolut (Absolute Zero)
ABSOLUTE_ZERO_CELSIUS: float = -273.15
ABSOLUTE_ZERO_FAHRENHEIT: float = -459.67
ABSOLUTE_ZERO_KELVIN: float = 0.0

# Faktor konversi untuk Fahrenheit
FAHRENHEIT_MULTIPLIER: float = 9/5  # Faktor pengali (9/5 atau 1.8)
FAHRENHEIT_OFFSET: int = 32  # Offset yang ditambahkan

# Faktor konversi untuk Kelvin
KELVIN_OFFSET: float = 273.15  # Offset yang ditambahkan/dikurangi

# Pesan error dan validasi
ERROR_INVALID_NUMBER: str = "❌ Input bukan angka yang valid!"
ERROR_BELOW_ABSOLUTE_ZERO: str = "❌ Suhu tidak bisa lebih rendah dari absolute zero!"
ERROR_INVALID_SCALE: str = "❌ Skala suhu tidak valid! Gunakan C, F, atau K."

# Pesan informasi
INFO_WELCOME: str = "🌡️  KONVERTER SUHU"
INFO_SEPARATOR: str = "=" * 50
INFO_INPUT_PROMPT: str = "Masukkan suhu yang ingin dikonversi: "
INFO_SCALE_PROMPT: str = "Pilih skala awal (C/F/K): "

# Simbol untuk setiap skala suhu
CELSIUS_SYMBOL: str = "°C"
FAHRENHEIT_SYMBOL: str = "°F"
KELVIN_SYMBOL: str = "K"

# Nama lengkap skala suhu (untuk display)
SCALE_NAMES: dict[str, str] = {
    "C": "Celsius",
    "F": "Fahrenheit",
    "K": "Kelvin"
}

# Precision untuk pembulatan hasil (jumlah desimal)
DECIMAL_PRECISION: int = 2