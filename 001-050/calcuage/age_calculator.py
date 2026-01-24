"""
Modul age_calculator.py
Modul ini bertanggung jawab untuk semua perhitungan yang berhubungan dengan umur.

Modul ini demonstrate penggunaan:
- Integer dan Float untuk perhitungan matematika
- Type conversion antara int dan float
- Dictionary untuk menyimpan hasil perhitungan terstruktur
"""

# Import fungsi-fungsi yang kita butuhkan dari modul date_utils
from date_utils import get_current_date, calculate_date_difference


def calculate_age_in_years(birth_date):
    """
    Fungsi untuk menghitung umur dalam tahun.
    
    Perhitungan umur yang akurat harus mempertimbangkan:
    - Apakah sudah ulang tahun di tahun ini
    - Jika belum, umur = tahun sekarang - tahun lahir - 1
    
    Args:
        birth_date (date): Object date tanggal lahir
        
    Returns:
        int: Umur dalam tahun
        
    Example:
        from datetime import date
        birth = date(2000, 5, 15)
        age = calculate_age_in_years(birth)
        print(age)  # Tergantung tanggal sekarang
    """
    
    # Ambil tanggal hari ini menggunakan fungsi dari date_utils
    # get_current_date() return object date
    today = get_current_date()
    
    # Hitung umur dasar: tahun sekarang dikurangi tahun lahir
    # today.year dan birth_date.year adalah integer
    # Hasil pengurangan integer dengan integer = integer
    age = today.year - birth_date.year
    
    # Check apakah sudah ulang tahun di tahun ini
    # Kita compare (month, day) sebagai tuple
    # Tuple comparison: membandingkan element per element dari kiri
    # Contoh: (5, 15) > (1, 22) karena 5 > 1
    # Contoh: (1, 25) > (1, 22) karena 1 = 1, tapi 25 > 22
    
    # Jika (bulan sekarang, hari sekarang) < (bulan lahir, hari lahir)
    # Berarti belum ulang tahun di tahun ini
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        # Kurangi 1 dari umur karena belum ulang tahun
        # Operator -= adalah shorthand untuk: age = age - 1
        age -= 1
    
    # Return umur dalam tahun sebagai integer
    return age


def calculate_total_days(birth_date):
    """
    Fungsi untuk menghitung total hari hidup sejak lahir.
    
    Args:
        birth_date (date): Object date tanggal lahir
        
    Returns:
        int: Total hari hidup
        
    Example:
        from datetime import date
        birth = date(2000, 1, 1)
        days = calculate_total_days(birth)
        print(days)  # Jumlah hari dari 2000-01-01 sampai hari ini
    """
    
    # Ambil tanggal hari ini
    today = get_current_date()
    
    # Hitung selisih tanggal menggunakan fungsi dari date_utils
    # calculate_date_difference() return object timedelta
    difference = calculate_date_difference(today, birth_date)
    
    # Object timedelta punya atribut .days yang berisi jumlah hari (integer)
    # Kita return nilai integer ini
    return difference.days


def calculate_total_hours(total_days):
    """
    Fungsi untuk menghitung total jam hidup.
    
    1 hari = 24 jam
    Total jam = total hari × 24
    
    Args:
        total_days (int): Total hari hidup
        
    Returns:
        int: Total jam hidup
        
    Example:
        hours = calculate_total_hours(9500)
        print(hours)  # 9500 * 24 = 228,000 jam
    """
    
    # Perkalian integer dengan integer menghasilkan integer
    # 1 hari = 24 jam, jadi total jam = total hari dikali 24
    # Operator * untuk perkalian
    return total_days * 24


def calculate_total_minutes(total_hours):
    """
    Fungsi untuk menghitung total menit hidup.
    
    1 jam = 60 menit
    Total menit = total jam × 60
    
    Args:
        total_hours (int): Total jam hidup
        
    Returns:
        int: Total menit hidup
        
    Example:
        minutes = calculate_total_minutes(228000)
        print(minutes)  # 228,000 * 60 = 13,680,000 menit
    """
    
    # 1 jam = 60 menit
    # Perkalian integer × integer = integer
    return total_hours * 60


def calculate_total_seconds(total_minutes):
    """
    Fungsi untuk menghitung total detik hidup.
    
    1 menit = 60 detik
    Total detik = total menit × 60
    
    Args:
        total_minutes (int): Total menit hidup
        
    Returns:
        int: Total detik hidup
        
    Example:
        seconds = calculate_total_seconds(13680000)
        print(seconds)  # 13,680,000 * 60 = 820,800,000 detik
    """
    
    # 1 menit = 60 detik
    # Perkalian integer × integer = integer
    return total_minutes * 60


def calculate_age_breakdown(birth_date):
    """
    Fungsi untuk menghitung breakdown umur dalam berbagai satuan waktu.
    
    Fungsi ini adalah "orchestrator" yang memanggil fungsi-fungsi lain
    dan mengumpulkan semua hasilnya dalam satu dictionary.
    
    Args:
        birth_date (date): Object date tanggal lahir
        
    Returns:
        dict: Dictionary berisi breakdown umur dengan key:
            - "years": Umur dalam tahun (int)
            - "total_days": Total hari hidup (int)
            - "total_hours": Total jam hidup (int)
            - "total_minutes": Total menit hidup (int)
            - "total_seconds": Total detik hidup (int)
            - "birth_date": Tanggal lahir (date)
            - "current_date": Tanggal hari ini (date)
            
    Example:
        from datetime import date
        birth = date(2000, 5, 15)
        breakdown = calculate_age_breakdown(birth)
        print(breakdown["years"])  # Umur dalam tahun
        print(breakdown["total_days"])  # Total hari hidup
    """
    
    # Hitung umur dalam tahun menggunakan fungsi yang sudah kita buat
    # calculate_age_in_years() return integer
    years = calculate_age_in_years(birth_date)
    
    # Hitung total hari hidup
    # calculate_total_days() return integer
    total_days = calculate_total_days(birth_date)
    
    # Hitung total jam hidup berdasarkan total hari
    # calculate_total_hours() return integer
    total_hours = calculate_total_hours(total_days)
    
    # Hitung total menit hidup berdasarkan total jam
    # calculate_total_minutes() return integer
    total_minutes = calculate_total_minutes(total_hours)
    
    # Hitung total detik hidup berdasarkan total menit
    # calculate_total_seconds() return integer
    total_seconds = calculate_total_seconds(total_minutes)
    
    # Ambil tanggal hari ini untuk disimpan di hasil
    current_date = get_current_date()
    
    # Buat dictionary untuk menyimpan semua hasil
    # Dictionary adalah struktur data key-value
    # Syntax: {key1: value1, key2: value2, ...}
    # Key bisa string, value bisa tipe data apapun
    # Dictionary memudahkan akses data dengan nama yang deskriptif
    breakdown = {
        "years": years,                    # int
        "total_days": total_days,          # int
        "total_hours": total_hours,        # int
        "total_minutes": total_minutes,    # int
        "total_seconds": total_seconds,    # int
        "birth_date": birth_date,          # date object
        "current_date": current_date,      # date object
    }
    
    # Return dictionary berisi semua informasi
    # Caller bisa akses dengan: breakdown["years"], breakdown["total_days"], dll
    return breakdown


def calculate_months_and_days(birth_date):
    """
    Fungsi untuk menghitung umur dalam format "X tahun, Y bulan, Z hari".
    
    Fungsi ini lebih kompleks karena harus menghitung:
    - Berapa tahun penuh
    - Dari sisa, berapa bulan penuh
    - Dari sisa lagi, berapa hari
    
    Args:
        birth_date (date): Object date tanggal lahir
        
    Returns:
        dict: Dictionary dengan key:
            - "years": Jumlah tahun penuh (int)
            - "months": Jumlah bulan setelah tahun penuh (int, 0-11)
            - "days": Jumlah hari setelah bulan penuh (int, 0-30)
            
    Example:
        from datetime import date
        birth = date(2000, 5, 15)
        result = calculate_months_and_days(birth)
        print(f"{result['years']} tahun, {result['months']} bulan, {result['days']} hari")
    """
    
    # Ambil tanggal hari ini
    today = get_current_date()
    
    # Hitung tahun penuh dulu menggunakan fungsi yang sudah ada
    # calculate_age_in_years() sudah handle kasus belum/sudah ulang tahun
    years = calculate_age_in_years(birth_date)
    
    # Hitung bulan
    # Cara: bulan sekarang - bulan lahir
    months = today.month - birth_date.month
    
    # Hitung hari
    # Cara: hari sekarang - hari lahir
    days = today.day - birth_date.day
    
    # Adjustment untuk hari
    # Jika hari sekarang < hari lahir (contoh: sekarang tgl 10, lahir tgl 15)
    # Berarti belum genap 1 bulan, kita harus mundur 1 bulan
    if days < 0:
        # Kurangi 1 bulan
        months -= 1
        
        # Hitung jumlah hari yang benar
        # Kita perlu tahu jumlah hari di bulan sebelumnya
        # Import fungsi get_days_in_month dari date_utils
        from date_utils import get_days_in_month
        
        # Hitung bulan sebelumnya
        # Jika bulan sekarang Januari (1), bulan sebelumnya = Desember tahun lalu
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        
        # Ambil jumlah hari di bulan sebelumnya
        days_in_prev_month = get_days_in_month(prev_year, prev_month)
        
        # Hitung hari yang benar
        # Contoh: sekarang tgl 10, lahir tgl 15, bulan lalu 30 hari
        # days = 10 - 15 = -5
        # days_correct = 30 + (-5) = 25 hari
        days = days_in_prev_month + days
    
    # Adjustment untuk bulan
    # Jika bulan < 0 (terjadi karena adjustment hari di atas)
    # Berarti kita harus mundur 1 tahun
    if months < 0:
        # Kurangi 1 tahun
        years -= 1
        # Tambah 12 bulan ke bulan negatif
        # Contoh: months = -2, maka months = 12 + (-2) = 10 bulan
        months += 12
    
    # Buat dictionary untuk return hasil
    # Semua value adalah integer
    result = {
        "years": years,      # int (0, 1, 2, ...)
        "months": months,    # int (0-11)
        "days": days,        # int (0-30)
    }
    
    # Return dictionary
    return result


# Testing modul jika file dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul age_calculator ===")
    print()
    
    # Import date untuk testing
    from datetime import date
    
    # Buat contoh tanggal lahir
    birth_date = date(2000, 5, 15)
    print(f"Tanggal lahir untuk testing: {birth_date}")
    print()
    
    # Test calculate_age_in_years()
    years = calculate_age_in_years(birth_date)
    print(f"Umur dalam tahun: {years} tahun")
    print()
    
    # Test calculate_total_days()
    total_days = calculate_total_days(birth_date)
    print(f"Total hari hidup: {total_days:,} hari")
    print()
    
    # Test calculate_age_breakdown()
    breakdown = calculate_age_breakdown(birth_date)
    print("Breakdown umur:")
    print(f"  Tahun: {breakdown['years']}")
    print(f"  Total hari: {breakdown['total_days']:,}")
    print(f"  Total jam: {breakdown['total_hours']:,}")
    print(f"  Total menit: {breakdown['total_minutes']:,}")
    print(f"  Total detik: {breakdown['total_seconds']:,}")
    print()
    
    # Test calculate_months_and_days()
    detailed = calculate_months_and_days(birth_date)
    print(f"Umur detail: {detailed['years']} tahun, {detailed['months']} bulan, {detailed['days']} hari")