"""
Modul date_utils.py
Modul ini bertanggung jawab untuk semua operasi yang berhubungan dengan tanggal dan waktu.

Di industri, pemisahan utility functions seperti ini membuat kode:
- Reusable (bisa dipakai di project lain)
- Testable (mudah di-test)
- Maintainable (mudah di-maintain)
"""

# Import library datetime untuk bekerja dengan tanggal dan waktu
# datetime adalah built-in library Python, tidak perlu install
# Kita import beberapa class yang kita butuhkan: datetime, date, timedelta
from datetime import datetime, date, timedelta


def get_current_date():
    """
    Fungsi untuk mendapatkan tanggal hari ini.
    
    Fungsi ini mengambil tanggal dari sistem komputer.
    Hasil berupa object date yang punya atribut: year, month, day.
    
    Returns:
        date: Object date yang merepresentasikan hari ini
        
    Example:
        today = get_current_date()
        print(today)  # 2026-01-22
        print(today.year)   # 2026
        print(today.month)  # 1
        print(today.day)    # 22
    """
    
    # date.today() adalah class method dari class date
    # Method ini return object date yang represent hari ini
    # Object date punya 3 atribut utama: year, month, day (semua integer)
    return date.today()


def create_date_from_string(date_string, date_format="%Y-%m-%d"):
    """
    Fungsi untuk membuat object date dari string.
    
    String tanggal seperti "2000-05-15" perlu diconvert ke object date
    agar bisa dilakukan operasi matematika (seperti menghitung selisih).
    
    Args:
        date_string (str): String tanggal, contoh: "2000-05-15"
        date_format (str): Format string tanggal (default: "%Y-%m-%d")
            %Y = Tahun 4 digit (2000)
            %m = Bulan 2 digit (01-12)
            %d = Hari 2 digit (01-31)
            
    Returns:
        date: Object date hasil parsing dari string
        None: Jika format tanggal salah atau tidak valid
        
    Example:
        birth_date = create_date_from_string("2000-05-15")
        print(birth_date)  # 2000-05-15
        
        # Format berbeda
        us_date = create_date_from_string("05/15/2000", "%m/%d/%Y")
    """
    
    # Try-except untuk handle kemungkinan error saat parsing tanggal
    # Error bisa terjadi jika format salah atau tanggal tidak valid
    try:
        # datetime.strptime() = string parse time
        # Method ini parse (membaca) string menjadi datetime object
        # strptime() mengambil 2 parameter:
        # 1. String yang mau di-parse
        # 2. Format string (pattern matching)
        datetime_obj = datetime.strptime(date_string, date_format)
        
        # datetime_obj adalah object datetime (punya date DAN time)
        # Kita hanya butuh date-nya saja, jadi kita ambil dengan .date()
        # .date() method return object date (tanpa informasi waktu)
        return datetime_obj.date()
        
    except ValueError as e:
        # ValueError terjadi jika:
        # - Format string tidak match (misal: "2000/05/15" tapi format "%Y-%m-%d")
        # - Tanggal tidak valid (misal: "2000-02-31" - Februari tidak ada tanggal 31)
        
        # Print error message untuk debugging
        # f-string memungkinkan kita embed variable dan expression
        print(f"❌ Error parsing tanggal: {e}")
        
        # Return None untuk indicate bahwa parsing gagal
        # Caller function harus check apakah hasilnya None atau bukan
        return None


def calculate_date_difference(date1, date2):
    """
    Fungsi untuk menghitung selisih antara dua tanggal.
    
    Fungsi ini melakukan operasi pengurangan antara dua object date.
    Hasilnya adalah object timedelta yang merepresentasikan durasi waktu.
    
    Args:
        date1 (date): Tanggal pertama (biasanya tanggal lebih baru)
        date2 (date): Tanggal kedua (biasanya tanggal lebih lama)
        
    Returns:
        timedelta: Object yang merepresentasikan selisih waktu
        
    Note:
        timedelta punya atribut .days untuk mendapat jumlah hari
        Jika date1 < date2, hasilnya negatif
        
    Example:
        today = date(2026, 1, 22)
        birthday = date(2000, 5, 15)
        diff = calculate_date_difference(today, birthday)
        print(diff.days)  # Jumlah hari antara dua tanggal
    """
    
    # Operasi pengurangan antara dua object date menghasilkan object timedelta
    # timedelta (time delta) = perbedaan/selisih waktu
    # timedelta object punya atribut:
    # - .days: jumlah hari (integer)
    # - .seconds: jumlah detik dalam hari terakhir (0-86399)
    # - .total_seconds(): total detik keseluruhan (float)
    
    # Contoh: date(2026, 1, 22) - date(2026, 1, 20) = timedelta(days=2)
    difference = date1 - date2
    
    # Return object timedelta
    # Caller bisa akses .days untuk dapat jumlah hari
    return difference


def is_valid_date(year, month, day):
    """
    Fungsi untuk memvalidasi apakah kombinasi tahun-bulan-hari adalah tanggal yang valid.
    
    Validasi penting untuk memastikan user input benar.
    Contoh invalid: 2000-02-31 (Februari tidak ada tanggal 31)
    Contoh invalid: 2000-13-01 (Bulan 13 tidak ada)
    
    Args:
        year (int): Tahun (contoh: 2000)
        month (int): Bulan (1-12)
        day (int): Hari (1-31, tergantung bulan)
        
    Returns:
        bool: True jika tanggal valid, False jika tidak
        
    Example:
        is_valid_date(2000, 2, 29)  # True (2000 tahun kabisat)
        is_valid_date(2001, 2, 29)  # False (2001 bukan tahun kabisat)
        is_valid_date(2000, 13, 1)  # False (bulan 13 tidak ada)
    """
    
    # Try-except pattern untuk validasi
    # Kita coba buat object date dengan parameter yang diberikan
    # Jika berhasil = valid, jika error = tidak valid
    try:
        # Coba buat object date dengan year, month, day yang diberikan
        # Constructor date() akan otomatis validasi:
        # - Apakah bulan antara 1-12
        # - Apakah hari sesuai dengan jumlah hari di bulan tersebut
        # - Apakah tahun kabisat (untuk Februari 29)
        date(year, month, day)
        
        # Jika tidak ada error, berarti tanggal valid
        # Return True untuk indicate valid
        return True
        
    except ValueError:
        # ValueError akan di-raise oleh date() jika parameter tidak valid
        # Contoh error message: "day is out of range for month"
        
        # Jika ada error, berarti tanggal tidak valid
        # Return False untuk indicate tidak valid
        return False


def get_days_in_month(year, month):
    """
    Fungsi untuk mendapatkan jumlah hari dalam bulan tertentu.
    
    Jumlah hari berbeda untuk setiap bulan:
    - Jan, Mar, May, Jul, Aug, Oct, Dec: 31 hari
    - Apr, Jun, Sep, Nov: 30 hari
    - Feb: 28 atau 29 hari (tergantung tahun kabisat)
    
    Args:
        year (int): Tahun (penting untuk cek tahun kabisat)
        month (int): Bulan (1-12)
        
    Returns:
        int: Jumlah hari dalam bulan tersebut
        None: Jika bulan tidak valid
        
    Example:
        get_days_in_month(2000, 2)  # 29 (2000 tahun kabisat)
        get_days_in_month(2001, 2)  # 28 (2001 bukan tahun kabisat)
        get_days_in_month(2000, 1)  # 31 (Januari selalu 31 hari)
    """
    
    # Validasi bulan harus antara 1-12
    # Operator 'or' akan return True jika salah satu kondisi True
    if month < 1 or month > 12:
        # Jika bulan tidak valid, return None
        return None
    
    # Trik untuk dapat jumlah hari dalam bulan:
    # Buat tanggal di bulan berikutnya, hari ke-1, lalu mundur 1 hari
    # Contoh: Bulan Feb 2000 = date(2000, 3, 1) - 1 hari = date(2000, 2, 29)
    
    # Jika bulan = 12 (Desember), bulan berikutnya = 1 (Januari tahun depan)
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        # Jika bukan Desember, tinggal tambah 1
        next_month = month + 1
        next_year = year
    
    # Buat tanggal: hari pertama bulan berikutnya
    first_day_next_month = date(next_year, next_month, 1)
    
    # Mundur 1 hari menggunakan timedelta
    # timedelta(days=1) = durasi 1 hari
    # Tanggal - 1 hari = tanggal kemarin = hari terakhir bulan ini
    last_day_current_month = first_day_next_month - timedelta(days=1)
    
    # Ambil atribut .day untuk dapat angka hari (28, 29, 30, atau 31)
    return last_day_current_month.day


# Testing modul jika file dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul date_utils ===")
    print()
    
    # Test get_current_date()
    today = get_current_date()
    print(f"Hari ini: {today}")
    print(f"Tahun: {today.year}, Bulan: {today.month}, Hari: {today.day}")
    print()
    
    # Test create_date_from_string()
    print("Test create_date_from_string():")
    birth_date = create_date_from_string("2000-05-15")
    print(f"Tanggal lahir dari string: {birth_date}")
    
    # Test dengan format berbeda
    us_date = create_date_from_string("05/15/2000", "%m/%d/%Y")
    print(f"Format US: {us_date}")
    
    # Test dengan string invalid
    invalid = create_date_from_string("2000-13-01")  # Bulan 13 tidak ada
    print(f"Tanggal invalid: {invalid}")  # Harusnya None
    print()
    
    # Test calculate_date_difference()
    print("Test calculate_date_difference():")
    diff = calculate_date_difference(today, birth_date)
    print(f"Selisih hari: {diff.days} hari")
    print()
    
    # Test is_valid_date()
    print("Test is_valid_date():")
    print(f"2000-02-29 valid? {is_valid_date(2000, 2, 29)}")  # True (kabisat)
    print(f"2001-02-29 valid? {is_valid_date(2001, 2, 29)}")  # False
    print(f"2000-13-01 valid? {is_valid_date(2000, 13, 1)}")  # False
    print()
    
    # Test get_days_in_month()
    print("Test get_days_in_month():")
    print(f"Feb 2000: {get_days_in_month(2000, 2)} hari")  # 29
    print(f"Feb 2001: {get_days_in_month(2001, 2)} hari")  # 28
    print(f"Jan 2000: {get_days_in_month(2000, 1)} hari")  # 31