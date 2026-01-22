"""
Modul quotes.py
Modul ini bertanggung jawab untuk menyimpan koleksi quote motivasi
dan menyediakan fungsi untuk mengambil quote secara random.

Docstring seperti ini (triple quotes) digunakan untuk dokumentasi modul/fungsi.
Ini adalah best practice di industri untuk menjelaskan tujuan kode.
"""

# Import library random yang sudah built-in di Python
# Library ini digunakan untuk menghasilkan pilihan acak/random
# Kita tidak perlu install library ini karena sudah tersedia di Python
import random


# Membuat list (daftar) yang berisi quote-quote motivasi
# List adalah struktur data yang bisa menyimpan banyak item dalam satu variabel
# Kita gunakan huruf besar MOTIVATIONAL_QUOTES karena ini adalah konstanta
# Konstanta = variabel yang nilainya tidak akan diubah selama program berjalan
# Konvensi penamaan: HURUF_BESAR_DENGAN_UNDERSCORE untuk konstanta
MOTIVATIONAL_QUOTES = [
    # Setiap item di dalam list dipisahkan dengan koma
    # String (teks) dibungkus dengan tanda kutip (bisa single ' atau double ")
    "Kesuksesan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan. - Colin Powell",
    
    "Jangan takut gagal, takutlah untuk tidak mencoba. - Michka Wibowo",
    
    "Kode yang baik adalah dokumentasinya sendiri. - Steve McConnell",
    
    "Programmer terbaik adalah mereka yang malas dengan cara yang cerdas. - Larry Wall",
    
    "Belajar coding bukan tentang menghapal syntax, tapi memahami logika. - Unknown",
    
    "Setiap expert programmer dulunya adalah pemula. Keep learning! - Unknown",
    
    "Bug adalah kesempatan untuk belajar lebih dalam. - Anonymous",
    
    "Code never lies, comments sometimes do. - Ron Jeffries",
]


def get_random_quote():
    """
    Fungsi untuk mengambil satu quote secara random dari list MOTIVATIONAL_QUOTES.
    
    Fungsi adalah blok kode yang dapat digunakan berulang kali.
    Kita mendefinisikan fungsi dengan keyword 'def' diikuti nama fungsi dan tanda kurung ().
    
    Returns:
        str: Sebuah string berisi quote motivasi yang dipilih secara acak
        
    Docstring fungsi menjelaskan:
    - Apa yang dilakukan fungsi
    - Parameter apa yang diterima (fungsi ini tidak menerima parameter)
    - Apa yang dikembalikan (return value)
    """
    
    # random.choice() adalah fungsi dari library random yang memilih
    # satu item secara acak dari list yang diberikan
    # Setiap kali fungsi ini dipanggil, bisa menghasilkan quote yang berbeda
    # Kita simpan hasil pilihan random ke variabel bernama 'quote'
    quote = random.choice(MOTIVATIONAL_QUOTES)
    
    # Keyword 'return' digunakan untuk mengembalikan nilai dari fungsi
    # Nilai yang dikembalikan bisa ditangkap oleh kode yang memanggil fungsi ini
    # Contoh: my_quote = get_random_quote() -> my_quote akan berisi quote yang random
    return quote


def get_all_quotes():
    """
    Fungsi untuk mengambil semua quote yang tersedia.
    
    Fungsi ini berguna jika kita ingin menampilkan semua quote,
    misalnya untuk fitur "lihat semua quote" di masa depan.
    
    Returns:
        list: List berisi semua quote motivasi yang tersedia
    """
    
    # Kita return langsung list MOTIVATIONAL_QUOTES
    # Fungsi ini tidak memodifikasi data, hanya mengembalikan referensi ke list
    return MOTIVATIONAL_QUOTES


def get_quote_count():
    """
    Fungsi untuk mengetahui jumlah total quote yang tersedia.
    
    Returns:
        int: Jumlah quote yang ada dalam koleksi
    """
    
    # len() adalah built-in function Python untuk menghitung panjang/jumlah item
    # Bisa digunakan untuk list, string, tuple, dictionary, dll
    # Hasilnya adalah integer (angka bulat) yang merepresentasikan jumlah item
    return len(MOTIVATIONAL_QUOTES)


# Blok kode ini hanya akan dijalankan jika file ini dijalankan langsung
# Tidak akan dijalankan jika file ini di-import sebagai modul di file lain
# __name__ adalah special variable yang otomatis dibuat Python
# Nilainya "__main__" jika file dijalankan langsung
# Nilainya nama modul (dalam hal ini "quotes") jika di-import
if __name__ == "__main__":
    # Ini adalah testing code untuk memastikan fungsi kita bekerja dengan baik
    # Good practice di industri: setiap modul punya test sederhana seperti ini
    
    print("=== Testing Modul Quotes ===")
    print()  # Print baris kosong untuk spacing yang lebih baik
    
    # Test fungsi get_quote_count()
    print(f"Total quote tersedia: {get_quote_count()}")
    print()
    
    # Test fungsi get_random_quote() - kita panggil 3 kali untuk lihat variasi
    print("Contoh random quotes:")
    print(f"1. {get_random_quote()}")
    print(f"2. {get_random_quote()}")
    print(f"3. {get_random_quote()}")
    print()
    
    # Test fungsi get_all_quotes()
    print("Semua quotes:")
    # Loop untuk menampilkan semua quote dengan nomor urut
    # enumerate() memberikan index (nomor urut) dan value (nilai item)
    # start=1 membuat penomoran dimulai dari 1, bukan 0
    for index, quote in enumerate(get_all_quotes(), start=1):
        print(f"{index}. {quote}")