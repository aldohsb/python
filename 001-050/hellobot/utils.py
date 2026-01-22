"""
Modul utils.py
Modul ini berisi fungsi-fungsi utility (pembantu) yang bersifat umum
dan bisa digunakan di berbagai bagian aplikasi.

Utils = utilities = fungsi-fungsi pembantu yang tidak spesifik ke satu fitur.
Di industri, file utils biasanya berisi fungsi-fungsi yang reusable.
"""

# Import library datetime untuk bekerja dengan tanggal dan waktu
# Library ini sudah built-in di Python, tidak perlu install
from datetime import datetime


def get_current_time_greeting():
    """
    Fungsi untuk mendapatkan sapaan berdasarkan waktu saat ini.
    
    Fungsi ini akan:
    - Mengecek jam berapa sekarang
    - Mengembalikan sapaan yang sesuai (Pagi/Siang/Sore/Malam)
    
    Returns:
        str: Sapaan berdasarkan waktu ("Pagi", "Siang", "Sore", atau "Malam")
    
    Contoh:
        Jika jam 08:00, return "Pagi"
        Jika jam 13:00, return "Siang"
    """
    
    # datetime.now() mengambil waktu sistem komputer saat ini (real-time)
    # Hasilnya adalah object datetime yang punya banyak atribut: year, month, day, hour, dll
    # .hour mengakses atribut jam dari object datetime (nilai 0-23)
    current_hour = datetime.now().hour
    
    # Conditional statement (if-elif-else) untuk logika pengambilan keputusan
    # Kita cek jam berapa sekarang dan return sapaan yang sesuai
    
    # Jika jam antara 5 pagi sampai sebelum jam 11 siang (5-10)
    # >= artinya "lebih besar atau sama dengan"
    # < artinya "lebih kecil dari" (tidak termasuk 11)
    if current_hour >= 5 and current_hour < 11:
        return "Pagi"
    
    # elif = else if, dicek jika kondisi if sebelumnya False
    # Jika jam antara 11 siang sampai sebelum jam 3 sore (11-14)
    elif current_hour >= 11 and current_hour < 15:
        return "Siang"
    
    # Jika jam antara 3 sore sampai sebelum jam 7 malam (15-18)
    elif current_hour >= 15 and current_hour < 19:
        return "Sore"
    
    # else akan dijalankan jika semua kondisi di atas False
    # Berarti jam 19-04 (malam hingga dini hari)
    else:
        return "Malam"


def clean_input(user_input):
    """
    Fungsi untuk membersihkan input dari user.
    
    Ketika user mengetik sesuatu, sering ada spasi berlebih di awal/akhir.
    Fungsi ini membersihkan input tersebut agar lebih rapi.
    
    Args:
        user_input (str): Input mentah dari user yang mungkin ada spasi berlebih
        
    Returns:
        str: Input yang sudah dibersihkan (spasi di awal/akhir dihapus, kapital di awal kata)
        
    Contoh:
        clean_input("  budi  ") -> "Budi"
        clean_input("andi susanto") -> "Andi Susanto"
    """
    
    # .strip() menghapus whitespace (spasi, tab, newline) di awal dan akhir string
    # Contoh: "  hello  ".strip() -> "hello"
    # .title() mengubah huruf pertama setiap kata menjadi kapital
    # Contoh: "budi santoso".title() -> "Budi Santoso"
    # Kita chain (menggabungkan) kedua method ini
    cleaned = user_input.strip().title()
    
    # Return hasil yang sudah dibersihkan
    return cleaned


def validate_not_empty(text):
    """
    Fungsi untuk memvalidasi bahwa input tidak kosong.
    
    Validasi input sangat penting di aplikasi untuk memastikan
    user memberikan data yang sesuai harapan.
    
    Args:
        text (str): Teks yang akan divalidasi
        
    Returns:
        bool: True jika teks tidak kosong, False jika kosong
        
    Contoh:
        validate_not_empty("Budi") -> True
        validate_not_empty("") -> False
        validate_not_empty("   ") -> False (hanya spasi dianggap kosong)
    """
    
    # .strip() dulu untuk hapus spasi, lalu cek apakah masih ada isinya
    # bool(string) akan return True jika string punya isi, False jika kosong
    # Atau bisa juga pakai: return len(text.strip()) > 0
    # Tapi cara di bawah lebih pythonic (idiom Python yang clean)
    return bool(text.strip())


def print_separator(char="=", length=50):
    """
    Fungsi untuk print garis pemisah visual di terminal.
    
    Pemisah visual membuat output lebih mudah dibaca.
    Fungsi ini flexible, bisa ubah karakter dan panjang garis.
    
    Args:
        char (str): Karakter yang digunakan untuk garis (default "=")
        length (int): Panjang garis yang akan di-print (default 50)
        
    Contoh:
        print_separator() -> ==================================================
        print_separator("-", 30) -> ------------------------------
        print_separator("*", 20) -> ********************
    """
    
    # Operator * untuk string akan mengulang string sejumlah yang ditentukan
    # Contoh: "=" * 5 menghasilkan "====="
    # Ini adalah cara pythonic untuk membuat string berulang
    print(char * length)


def format_display_text(text, width=50, fill_char=" ", align="center"):
    """
    Fungsi untuk memformat teks dengan lebar tertentu dan alignment.
    
    Fungsi ini berguna untuk membuat tampilan yang rapi dan centered.
    
    Args:
        text (str): Teks yang akan diformat
        width (int): Lebar total tampilan (default 50)
        fill_char (str): Karakter pengisi di sisi kiri/kanan (default spasi)
        align (str): Alignment - "center", "left", atau "right" (default "center")
        
    Returns:
        str: Teks yang sudah diformat
        
    Contoh:
        format_display_text("Hello", 20, align="center") -> "       Hello        "
        format_display_text("Hello", 20, "*", "center") -> "*******Hello********"
    """
    
    # String punya method built-in untuk alignment
    # .center() membuat teks di tengah dengan padding
    # .ljust() membuat teks rata kiri (left justified)
    # .rjust() membuat teks rata kanan (right justified)
    
    if align == "center":
        # .center(width, fillchar) menempatkan teks di tengah
        # dan mengisi sisa space dengan fillchar
        return text.center(width, fill_char)
    elif align == "left":
        # .ljust(width, fillchar) meratakan teks ke kiri
        return text.ljust(width, fill_char)
    elif align == "right":
        # .rjust(width, fillchar) meratakan teks ke kanan
        return text.rjust(width, fill_char)
    else:
        # Default jika align tidak valid, return center
        return text.center(width, fill_char)


# Testing modul jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul Utils ===")
    print()
    
    # Test get_current_time_greeting()
    current_greeting = get_current_time_greeting()
    current_time = datetime.now().strftime("%H:%M:%S")  # Format jam:menit:detik
    print(f"Waktu sekarang: {current_time}")
    print(f"Sapaan yang sesuai: {current_greeting}")
    print()
    
    # Test clean_input()
    test_inputs = ["  budi  ", "ANDI SUSANTO", "  maria  clara  "]
    print("Test clean_input():")
    for test_input in test_inputs:
        cleaned = clean_input(test_input)
        print(f"Input: '{test_input}' -> Output: '{cleaned}'")
    print()
    
    # Test validate_not_empty()
    print("Test validate_not_empty():")
    test_validations = ["Budi", "", "   ", "A"]
    for test_val in test_validations:
        is_valid = validate_not_empty(test_val)
        print(f"Input: '{test_val}' -> Valid: {is_valid}")
    print()
    
    # Test print_separator()
    print("Test print_separator():")
    print_separator()
    print_separator("-", 30)
    print_separator("*", 20)
    print()
    
    # Test format_display_text()
    print("Test format_display_text():")
    print(format_display_text("HELLO", 30, align="center"))
    print(format_display_text("HELLO", 30, "*", "center"))
    print(format_display_text("HELLO", 30, align="left"))
    print(format_display_text("HELLO", 30, align="right"))