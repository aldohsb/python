"""
Modul input_handler.py
Modul ini bertanggung jawab untuk menangani dan memvalidasi semua input dari user.

Input validation adalah salah satu aspek terpenting dalam programming:
- Mencegah error/crash akibat input yang tidak valid
- Memberikan user experience yang baik dengan pesan error yang jelas
- Memastikan data yang masuk ke sistem sudah sesuai format

Modul ini demonstrate:
- Type conversion (string to integer)
- Input validation dengan multiple checks
- Error handling dengan try-except
- Loop untuk retry input yang invalid
"""

# Import fungsi-fungsi yang kita butuhkan
from date_utils import is_valid_date, create_date_from_string, get_current_date


def get_integer_input(prompt, min_value=None, max_value=None):
    """
    Fungsi untuk mendapatkan input integer dari user dengan validasi.
    
    Fungsi ini akan:
    1. Meminta input dari user
    2. Validasi bahwa input adalah angka (bisa diconvert ke integer)
    3. Validasi bahwa angka dalam range yang diperbolehkan (jika ada min/max)
    4. Terus meminta ulang sampai input valid
    
    Args:
        prompt (str): Pesan yang ditampilkan ke user
        min_value (int, optional): Nilai minimum yang diperbolehkan
        max_value (int, optional): Nilai maksimum yang diperbolehkan
        
    Returns:
        int: Input user yang sudah valid dan diconvert ke integer
        
    Example:
        umur = get_integer_input("Masukkan umur: ", min_value=0, max_value=150)
        bulan = get_integer_input("Bulan lahir (1-12): ", 1, 12)
    """
    
    # Loop tak terbatas sampai mendapat input yang valid
    # while True akan terus berjalan sampai ada 'break' atau 'return'
    while True:
        # Ambil input dari user sebagai string
        # input() function selalu return string, apapun yang user ketik
        user_input = input(prompt)
        
        # Try-except untuk handle error saat convert string ke integer
        # Error bisa terjadi jika user input bukan angka (misal: "abc", "12.5")
        try:
            # Coba convert string ke integer
            # int() akan raise ValueError jika string tidak bisa diconvert
            # Contoh sukses: int("25") -> 25
            # Contoh error: int("abc") -> ValueError
            # Contoh error: int("12.5") -> ValueError (ada titik desimal)
            value = int(user_input)
            
            # Validasi minimum value jika parameter min_value diberikan
            # min_value is not None = True jika min_value ada nilai (tidak None)
            # Operator 'is not' untuk compare dengan None (best practice)
            if min_value is not None and value < min_value:
                # Jika value kurang dari minimum, tampilkan error
                # f-string untuk embed variable dalam string
                print(f"❌ Nilai harus minimal {min_value}")
                # continue akan skip sisa code dan kembali ke awal loop
                # Loop akan mengulang dan meminta input lagi
                continue
            
            # Validasi maximum value jika parameter max_value diberikan
            if max_value is not None and value > max_value:
                # Jika value lebih dari maksimum, tampilkan error
                print(f"❌ Nilai harus maksimal {max_value}")
                # continue untuk mengulang loop
                continue
            
            # Jika semua validasi passed, return value
            # return akan menghentikan loop dan function
            return value
            
        except ValueError:
            # ValueError terjadi saat int() gagal convert string
            # Contoh: user input "abc", "dua puluh", "12.5"
            print("❌ Input harus berupa angka bulat. Silakan coba lagi.")
            # Loop akan mengulang otomatis (tidak perlu continue eksplisit)


def get_birth_date_input():
    """
    Fungsi untuk mendapatkan tanggal lahir dari user dengan validasi lengkap.
    
    Fungsi ini akan:
    1. Meminta tahun, bulan, hari lahir secara terpisah
    2. Validasi setiap input (must be integer, valid range)
    3. Validasi kombinasi tahun-bulan-hari (tanggal valid?)
    4. Validasi tanggal tidak di masa depan
    5. Terus meminta ulang sampai semua valid
    
    Returns:
        date: Object date tanggal lahir yang valid
        
    Example:
        birth_date = get_birth_date_input()
        print(birth_date)  # 2000-05-15
    """
    
    # Loop tak terbatas sampai mendapat tanggal lahir yang valid
    while True:
        print("\n📅 Masukkan tanggal lahir Anda:")
        print("=" * 50)
        
        # Ambil tahun lahir dengan validasi
        # get_integer_input() sudah handle validasi integer dan range
        # Range tahun: 1900 - tahun sekarang (tidak bisa lahir di masa depan)
        current_year = get_current_date().year
        year = get_integer_input(
            "Tahun lahir (contoh: 2000): ",
            min_value=1900,
            max_value=current_year
        )
        
        # Ambil bulan lahir dengan validasi
        # Range bulan: 1-12 (Januari-Desember)
        month = get_integer_input(
            "Bulan lahir (1-12): ",
            min_value=1,
            max_value=12
        )
        
        # Ambil hari lahir dengan validasi
        # Range hari: 1-31 (validasi lebih detail akan dilakukan setelah ini)
        day = get_integer_input(
            "Tanggal lahir (1-31): ",
            min_value=1,
            max_value=31
        )
        
        # Validasi kombinasi tahun-bulan-hari
        # is_valid_date() check apakah tanggal benar-benar ada
        # Contoh invalid: 2023-02-31 (Feb tidak ada tgl 31)
        # Contoh invalid: 2023-04-31 (April hanya sampai tgl 30)
        if not is_valid_date(year, month, day):
            # Jika kombinasi tidak valid, tampilkan error dan ulangi
            print(f"\n❌ Tanggal {year}-{month:02d}-{day:02d} tidak valid.")
            print("💡 Tips: Periksa jumlah hari di bulan tersebut.")
            # continue untuk mengulang loop dari awal
            continue
        
        # Buat object date dari input yang sudah valid
        # Format string: YYYY-MM-DD (ISO 8601 standard)
        # :02d = format integer dengan 2 digit, tambah leading zero jika perlu
        # Contoh: month=5 -> "05", day=7 -> "07"
        date_string = f"{year}-{month:02d}-{day:02d}"
        
        # Convert string ke object date
        # create_date_from_string() return object date atau None jika error
        birth_date = create_date_from_string(date_string)
        
        # Double check apakah conversion berhasil
        # Seharusnya tidak None karena sudah validasi, tapi safety check
        if birth_date is None:
            print("\n❌ Terjadi error saat memproses tanggal. Silakan coba lagi.")
            continue
        
        # Validasi tanggal tidak di masa depan
        # Tidak mungkin seseorang lahir di masa depan
        today = get_current_date()
        if birth_date > today:
            # Operator > bisa digunakan untuk compare date objects
            # birth_date > today = True jika birth_date lebih baru dari today
            print(f"\n❌ Tanggal lahir tidak bisa di masa depan!")
            print(f"Hari ini: {today}")
            continue
        
        # Jika semua validasi passed, return tanggal lahir
        # Tampilkan konfirmasi dulu
        print(f"\n✅ Tanggal lahir: {birth_date.strftime('%d %B %Y')}")
        # strftime = string format time, untuk format tanggal lebih readable
        # %d = day (01-31), %B = full month name, %Y = year (4 digit)
        
        # Return object date
        return birth_date


def get_yes_no_input(prompt):
    """
    Fungsi untuk mendapatkan input Yes/No dari user.
    
    Fungsi ini menerima berbagai variasi jawaban:
    - Yes: "y", "yes", "ya", "iya" (case-insensitive)
    - No: "n", "no", "tidak", "tidak" (case-insensitive)
    
    Args:
        prompt (str): Pesan yang ditampilkan ke user
        
    Returns:
        bool: True jika user menjawab Yes, False jika No
        
    Example:
        want_continue = get_yes_no_input("Lanjutkan? (y/n): ")
        if want_continue:
            print("Melanjutkan...")
        else:
            print("Berhenti...")
    """
    
    # Loop sampai mendapat jawaban yang valid
    while True:
        # Ambil input dari user
        user_input = input(prompt)
        
        # Bersihkan input: lowercase dan strip whitespace
        # .strip() menghapus spasi di awal/akhir
        # .lower() convert semua huruf ke lowercase
        # Chain method call: hasil strip() langsung di-lower()
        cleaned_input = user_input.strip().lower()
        
        # Check apakah jawaban adalah Yes
        # Operator 'in' check apakah value ada dalam list/tuple
        # cleaned_input in (...) return True jika cleaned_input salah satu dari values
        if cleaned_input in ("y", "yes", "ya", "iya"):
            # Return True untuk indicate Yes
            return True
        
        # Check apakah jawaban adalah No
        elif cleaned_input in ("n", "no", "tidak", "tak"):
            # Return False untuk indicate No
            return False
        
        # Jika jawaban tidak recognized, tampilkan error dan ulangi
        else:
            print("❌ Input tidak valid. Silakan jawab dengan y/n atau yes/no")
            # Loop akan mengulang otomatis


def confirm_birth_date(birth_date):
    """
    Fungsi untuk konfirmasi tanggal lahir dengan user.
    
    Best practice: Selalu confirm data penting dengan user
    untuk memastikan tidak ada kesalahan input.
    
    Args:
        birth_date (date): Object date tanggal lahir yang akan dikonfirmasi
        
    Returns:
        bool: True jika user confirm, False jika ingin ubah
        
    Example:
        if confirm_birth_date(birth_date):
            print("Tanggal lahir confirmed")
        else:
            print("Silakan input ulang")
    """
    
    # Format tanggal dengan readable format
    # strftime() untuk custom format tanggal
    # %A = full weekday name, %d = day, %B = full month name, %Y = year
    formatted_date = birth_date.strftime("%A, %d %B %Y")
    
    # Tampilkan tanggal dan minta konfirmasi
    print(f"\n📅 Tanggal lahir Anda: {formatted_date}")
    
    # Gunakan get_yes_no_input() untuk minta konfirmasi
    # Return langsung hasilnya (True atau False)
    return get_yes_no_input("Apakah tanggal ini sudah benar? (y/n): ")


# Testing modul jika file dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul input_handler ===")
    print()
    
    # Test get_integer_input()
    print("Test get_integer_input():")
    print("Silakan input angka antara 1-10")
    num = get_integer_input("Angka: ", min_value=1, max_value=10)
    print(f"Anda input: {num}")
    print()
    
    # Test get_birth_date_input()
    print("Test get_birth_date_input():")
    birth = get_birth_date_input()
    print(f"Tanggal lahir: {birth}")
    print()
    
    # Test confirm_birth_date()
    print("Test confirm_birth_date():")
    confirmed = confirm_birth_date(birth)
    print(f"Confirmed: {confirmed}")
    print()
    
    # Test get_yes_no_input()
    print("Test get_yes_no_input():")
    answer = get_yes_no_input("Apakah Anda suka Python? (y/n): ")
    if answer:
        print("Wah, sama! Python memang keren! 🐍")
    else:
        print("Tidak apa-apa, mungkin nanti suka 😊")