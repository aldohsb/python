"""
main.py - Entry Point HelloBot Application

File ini adalah entry point (pintu masuk) aplikasi HelloBot.
Entry point adalah file yang pertama kali dijalankan ketika aplikasi distart.

Di industri, main.py biasanya:
- Mengatur flow utama aplikasi
- Mengkoordinasikan modul-modul lain
- Menangani error handling di level tertinggi
- Minimal business logic (logika bisnis ada di modul terpisah)

Aplikasi HelloBot ini mendemonstrasikan:
1. Modular programming (kode terpisah berdasarkan fungsi)
2. Import antar modul
3. User interaction (input/output)
4. Random selection
5. Best practices Python
"""

# Import semua fungsi yang kita butuhkan dari modul-modul yang sudah kita buat
# Setiap modul punya tanggung jawab spesifik (separation of concerns)

# Dari modul greetings: fungsi-fungsi untuk sapaan dan banner
from greetings import display_welcome_banner, display_goodbye_banner, get_user_name

# Dari modul quotes: fungsi untuk mengambil quote motivasi
from quotes import get_random_quote, get_quote_count

# Dari modul utils: fungsi utility untuk formatting
from utils import print_separator, format_display_text


def display_quote_section(user_name):
    """
    Fungsi untuk menampilkan section quote motivasi.
    
    Fungsi ini bertanggung jawab untuk:
    - Menampilkan header section quote
    - Mengambil quote random
    - Menampilkan quote dengan format yang menarik
    
    Args:
        user_name (str): Nama user untuk personalisasi pesan
        
    Side Effect:
        Mencetak quote section ke terminal
        
    Design Decision:
        Kita buat fungsi terpisah untuk display quote agar:
        1. Kode lebih modular dan reusable
        2. Mudah di-maintain jika mau ubah format tampilan
        3. Bisa di-test secara terpisah
        4. Main function tidak terlalu panjang
    """
    
    # Print line kosong untuk spacing visual yang lebih baik
    print()
    
    # Print header section quote dengan separator
    print_separator()
    
    # Buat pesan header yang personal menggunakan f-string
    # F-string memungkinkan kita embed variable langsung di dalam string
    header_message = f"💡 Quote Motivasi untuk {user_name}"
    
    # Format header agar centered dengan lebar 50 karakter
    # format_display_text() ada di modul utils
    print(format_display_text(header_message, width=50))
    
    # Print separator lagi untuk pemisah visual
    print_separator()
    
    # Print line kosong
    print()
    
    # Ambil satu quote random menggunakan fungsi dari modul quotes
    # get_random_quote() akan return string berisi quote
    # Setiap kali dipanggil bisa menghasilkan quote yang berbeda
    quote = get_random_quote()
    
    # Print quote dengan indentasi untuk visual yang lebih baik
    # "  " (2 spasi) di awal untuk indentasi
    print(f"  {quote}")
    
    # Print line kosong
    print()
    
    # Print informasi berapa total quote yang tersedia
    # get_quote_count() return integer jumlah quote
    total_quotes = get_quote_count()
    info_message = f"(Salah satu dari {total_quotes} quote motivasi)"
    
    # Print info dengan format centered
    print(format_display_text(info_message, width=50))
    
    # Print line kosong
    print()


def display_features_info():
    """
    Fungsi untuk menampilkan informasi fitur-fitur HelloBot.
    
    Fungsi ini menjelaskan ke user apa saja yang bisa dilakukan HelloBot.
    Good UX practice: user harus tahu apa yang bisa dilakukan aplikasi.
    
    Side Effect:
        Mencetak informasi fitur ke terminal
    """
    
    # Print line kosong
    print()
    
    # Print separator
    print_separator("-", 50)
    
    # Print header fitur
    features_header = "✨ Fitur HelloBot"
    print(format_display_text(features_header, width=50))
    
    # Print separator
    print_separator("-", 50)
    
    # List fitur-fitur yang tersedia
    # Di versi sederhana ini hanya ada satu fitur, tapi struktur ini
    # memudahkan untuk menambah fitur baru di masa depan
    features = [
        "✅ Sapaan personal berdasarkan waktu",
        "✅ Quote motivasi random untuk semangat harimu",
        "✅ Interface yang friendly dan menarik",
    ]
    
    # Loop untuk print setiap fitur
    # Kita gunakan for loop untuk iterasi melalui list
    print()
    for feature in features:
        # Print setiap fitur dengan indentasi
        print(f"  {feature}")
    
    # Print line kosong
    print()
    
    # Print separator
    print_separator("-", 50)
    
    # Print line kosong
    print()


def run_hellobot():
    """
    Fungsi utama yang menjalankan aplikasi HelloBot.
    
    Fungsi ini adalah core logic aplikasi yang:
    1. Meminta nama user
    2. Menampilkan welcome banner
    3. Menampilkan informasi fitur
    4. Menampilkan quote motivasi
    5. Menampilkan goodbye banner
    
    Design Pattern:
        Ini adalah "orchestrator function" yang mengkoordinasikan
        fungsi-fungsi lain tanpa terlalu banyak detail implementasi.
        Detail implementasi ada di fungsi-fungsi yang dipanggil.
        
    Error Handling:
        Dalam versi production, kita akan tambah try-except untuk
        handle error yang mungkin terjadi. Untuk pembelajaran,
        kita keep it simple dulu.
    """
    
    # STEP 1: Ambil nama user
    # get_user_name() akan loop sampai user memberikan nama yang valid
    # Fungsi ini return string nama yang sudah dibersihkan
    user_name = get_user_name()
    
    # STEP 2: Tampilkan welcome banner dengan nama user
    # display_welcome_banner() tidak return apa-apa, langsung print
    display_welcome_banner(user_name)
    
    # STEP 3: Tampilkan informasi fitur-fitur HelloBot
    # Ini memberikan konteks ke user tentang apa yang akan mereka dapatkan
    display_features_info()
    
    # STEP 4: Tampilkan section quote motivasi
    # display_quote_section() akan mengambil dan menampilkan quote random
    display_quote_section(user_name)
    
    # STEP 5: Tampilkan goodbye banner
    # Menutup interaksi dengan pesan perpisahan yang friendly
    display_goodbye_banner(user_name)


def main():
    """
    Main function - Entry point ketika script dijalankan.
    
    Fungsi ini adalah best practice untuk Python application.
    Dengan punya fungsi main(), kode kita:
    1. Lebih terstruktur
    2. Mudah di-import sebagai modul jika diperlukan
    3. Bisa di-test dengan lebih mudah
    4. Mengikuti konvensi industri
    
    Di banyak framework dan library Python, pattern ini sangat umum.
    """
    
    # Kita bisa tambahkan try-except di sini untuk error handling
    # Tapi untuk learning purpose, kita keep simple
    # Contoh dengan error handling:
    # try:
    #     run_hellobot()
    # except KeyboardInterrupt:
    #     print("\n\nProgram dihentikan oleh user. Bye!")
    # except Exception as e:
    #     print(f"\n\nTerjadi error: {e}")
    
    # Untuk sekarang, langsung panggil run_hellobot()
    run_hellobot()


# Special Python idiom: if __name__ == "__main__"
# Ini adalah pattern yang sangat penting di Python
#
# Penjelasan:
# - __name__ adalah special variable yang otomatis ada di setiap file Python
# - Jika file dijalankan langsung: __name__ = "__main__"
# - Jika file di-import sebagai modul: __name__ = nama file (tanpa .py)
#
# Contoh:
# - python main.py -> __name__ = "__main__" -> kode di bawah dijalankan
# - import main (di file lain) -> __name__ = "main" -> kode di bawah TIDAK dijalankan
#
# Kenapa ini penting?
# - Memisahkan "script mode" vs "module mode"
# - Membuat file bisa dual-purpose: dijalankan langsung ATAU di-import
# - Best practice di Python untuk semua executable scripts
if __name__ == "__main__":
    # Blok ini hanya dijalankan jika file ini dijalankan langsung
    # Tidak dijalankan jika file ini di-import
    
    # Panggil fungsi main() untuk start aplikasi
    # Dengan memisahkan main() dan if __name__ == "__main__",
    # kita bisa test main() secara terpisah jika diperlukan
    main()
    
    # Fun fact: Di beberapa perusahaan, main.py bahkan lebih minimal lagi
    # Hanya import dan panggil fungsi dari modul lain
    # Semua logic ada di modul-modul terpisah
    # Ini membuat testing lebih mudah dan kode lebih maintainable