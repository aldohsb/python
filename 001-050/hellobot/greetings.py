"""
Modul greetings.py
Modul ini bertanggung jawab untuk semua fungsi yang berhubungan dengan sapaan/greeting.

Dengan memisahkan concern (tanggung jawab) ke modul terpisah,
kode menjadi lebih modular, mudah di-maintain, dan mudah di-test.
Ini adalah prinsip "Separation of Concerns" yang penting di software engineering.
"""

# Import fungsi dari modul utils yang sudah kita buat sebelumnya
# Kita hanya import fungsi yang kita butuhkan, bukan import semua isi modul
# Ini membuat kode lebih eksplisit dan efisien
from utils import get_current_time_greeting, format_display_text, print_separator


def create_welcome_message(name):
    """
    Fungsi untuk membuat pesan sambutan yang personal untuk user.
    
    Fungsi ini akan:
    - Mengambil sapaan berdasarkan waktu saat ini
    - Membuat pesan welcome yang dipersonalisasi dengan nama user
    
    Args:
        name (str): Nama user yang akan disambut
        
    Returns:
        str: Pesan sambutan yang sudah dipersonalisasi
        
    Contoh:
        Jika nama="Budi" dan waktu pagi:
        return "Selamat Pagi, Budi! 👋"
    """
    
    # Memanggil fungsi get_current_time_greeting() dari modul utils
    # Fungsi ini akan return "Pagi", "Siang", "Sore", atau "Malam"
    # berdasarkan waktu sistem saat ini
    time_greeting = get_current_time_greeting()
    
    # F-string (formatted string literal) untuk membuat string dengan variable
    # Syntax: f"teks {variable} teks lagi"
    # Variable di dalam {} akan di-evaluate dan dimasukkan ke dalam string
    # Emoji 👋 membuat pesan lebih friendly dan modern
    message = f"Selamat {time_greeting}, {name}! 👋"
    
    # Return pesan yang sudah dibuat
    return message


def create_goodbye_message(name):
    """
    Fungsi untuk membuat pesan perpisahan yang personal.
    
    Args:
        name (str): Nama user yang akan dipamit
        
    Returns:
        str: Pesan perpisahan yang personal
        
    Contoh:
        create_goodbye_message("Budi") -> "Sampai jumpa lagi, Budi! Semangat terus belajarnya! 🚀"
    """
    
    # Membuat pesan goodbye dengan emoji untuk kesan friendly
    # \n adalah escape sequence untuk newline (baris baru)
    # Tapi di fungsi ini kita tidak pakai \n, biar flexibel penggunaannya
    message = f"Sampai jumpa lagi, {name}! Semangat terus belajarnya! 🚀"
    
    return message


def display_welcome_banner(name):
    """
    Fungsi untuk menampilkan banner welcome yang menarik.
    
    Banner ini membuat aplikasi terlihat lebih profesional dan user-friendly.
    Fungsi ini tidak return apa-apa, langsung print ke terminal.
    
    Args:
        name (str): Nama user yang akan ditampilkan di banner
        
    Side Effect:
        Mencetak banner ke terminal (stdout)
    """
    
    # Print line kosong untuk spacing yang lebih baik
    print()
    
    # Print garis pemisah atas menggunakan fungsi dari utils
    # print_separator() default menggunakan "=" sepanjang 50 karakter
    print_separator()
    
    # Print judul aplikasi dengan format centered
    # format_display_text() dari utils akan membuat text di tengah
    # width=50 agar sesuai dengan panjang separator
    title = format_display_text("🤖 HELLOBOT 🤖", width=50)
    print(title)
    
    # Print subtitle
    subtitle = format_display_text("Your Friendly Motivation Companion", width=50)
    print(subtitle)
    
    # Print garis pemisah tengah
    print_separator()
    
    # Print line kosong untuk spacing
    print()
    
    # Print pesan welcome menggunakan fungsi create_welcome_message
    welcome = create_welcome_message(name)
    # Center-aligned welcome message
    print(format_display_text(welcome, width=50))
    
    # Print line kosong lagi
    print()


def display_goodbye_banner(name):
    """
    Fungsi untuk menampilkan banner goodbye yang menarik.
    
    Args:
        name (str): Nama user yang akan ditampilkan di banner goodbye
        
    Side Effect:
        Mencetak banner goodbye ke terminal
    """
    
    # Print line kosong untuk spacing
    print()
    
    # Print garis pemisah
    print_separator()
    
    # Print pesan goodbye menggunakan fungsi create_goodbye_message
    goodbye = create_goodbye_message(name)
    print(format_display_text(goodbye, width=50))
    
    # Print pesan tambahan
    thank_you = "Terima kasih sudah menggunakan HelloBot!"
    print(format_display_text(thank_you, width=50))
    
    # Print garis pemisah bawah
    print_separator()
    
    # Print line kosong
    print()


def get_user_name():
    """
    Fungsi untuk meminta nama dari user melalui input.
    
    Fungsi ini akan:
    - Meminta user memasukkan nama
    - Memvalidasi bahwa nama tidak kosong
    - Terus meminta sampai user memberikan nama yang valid
    
    Returns:
        str: Nama user yang sudah valid dan dibersihkan
        
    Note:
        Fungsi ini menggunakan loop sampai mendapat input yang valid.
        Ini adalah pattern "input validation" yang umum di programming.
    """
    
    # Loop while True akan terus berjalan sampai ada statement 'break' atau 'return'
    # Ini adalah pattern umum untuk input validation
    while True:
        # input() adalah built-in function untuk membaca input dari user
        # Parameter adalah prompt (teks yang ditampilkan ke user)
        # Fungsi ini akan menunggu user mengetik sesuatu dan tekan Enter
        # Hasil dari input() adalah string
        name = input("Siapa nama Anda? ")
        
        # Import fungsi validate_not_empty dari utils untuk validasi
        # Kita import di dalam fungsi (bukan di atas) untuk menghindari circular import
        # jika diperlukan, meskipun dalam kasus ini bisa juga di-import di atas
        from utils import validate_not_empty, clean_input
        
        # Validasi apakah nama tidak kosong
        # validate_not_empty() return True jika valid, False jika tidak
        if validate_not_empty(name):
            # Jika nama valid, bersihkan nama menggunakan clean_input
            # clean_input() akan:
            # 1. Menghapus spasi di awal dan akhir
            # 2. Membuat huruf pertama setiap kata menjadi kapital (title case)
            cleaned_name = clean_input(name)
            
            # Return nama yang sudah bersih
            # Ketika fungsi return, loop langsung berhenti
            return cleaned_name
        else:
            # Jika nama tidak valid (kosong atau hanya spasi)
            # Tampilkan pesan error dan loop akan mengulang
            # Loop kembali ke atas dan meminta input lagi
            print("❌ Nama tidak boleh kosong. Silakan coba lagi.")
            print()  # Print baris kosong untuk spacing


# Testing modul jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul Greetings ===")
    print()
    
    # Test create_welcome_message()
    test_name = "Budi Santoso"
    welcome_msg = create_welcome_message(test_name)
    print(f"Test create_welcome_message(): {welcome_msg}")
    print()
    
    # Test create_goodbye_message()
    goodbye_msg = create_goodbye_message(test_name)
    print(f"Test create_goodbye_message(): {goodbye_msg}")
    print()
    
    # Test display_welcome_banner()
    print("Test display_welcome_banner():")
    display_welcome_banner(test_name)
    
    # Test display_goodbye_banner()
    print("Test display_goodbye_banner():")
    display_goodbye_banner(test_name)
    
    # Test get_user_name() - COMMENTED karena butuh user interaction
    # Uncomment baris di bawah jika ingin test interaktif
    # print("Test get_user_name():")
    # user_name = get_user_name()
    # print(f"Nama yang diinput: {user_name}")