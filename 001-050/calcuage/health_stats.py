"""
Modul health_stats.py
Modul ini bertanggung jawab untuk menghitung statistik kesehatan yang menarik.

Modul ini demonstrate:
- Penggunaan konstanta untuk nilai-nilai tetap
- Perhitungan matematika dengan integer dan float
- Type conversion antara int dan float
- Formatting angka besar agar mudah dibaca
"""

# Konstanta untuk rata-rata detak jantung dan pernapasan
# Konstanta ditulis dengan HURUF_BESAR_SEMUA (PEP 8 convention)
# Konstanta adalah variabel yang nilainya tidak boleh diubah

# Rata-rata detak jantung normal orang dewasa dalam kondisi istirahat
# Satuan: beats per minute (bpm)
# Source: American Heart Association
AVERAGE_HEART_RATE_BPM = 72

# Rata-rata frekuensi pernapasan normal orang dewasa
# Satuan: breaths per minute
# Source: American Lung Association
AVERAGE_BREATHING_RATE_PER_MINUTE = 16

# Rata-rata waktu tidur yang direkomendasikan untuk orang dewasa
# Satuan: jam per hari
# Source: National Sleep Foundation
AVERAGE_SLEEP_HOURS_PER_DAY = 8

# Rata-rata jumlah langkah yang direkomendasikan per hari
# Satuan: langkah (steps)
# Source: WHO (World Health Organization)
RECOMMENDED_STEPS_PER_DAY = 10000


def calculate_heartbeats(total_minutes):
    """
    Fungsi untuk menghitung estimasi total detak jantung sejak lahir.
    
    Rumus: Total detak = Total menit × Detak per menit
    
    Catatan: Ini adalah estimasi kasar menggunakan rata-rata.
    Detak jantung sesungguhnya bervariasi tergantung aktivitas, kesehatan, dll.
    
    Args:
        total_minutes (int): Total menit hidup
        
    Returns:
        int: Estimasi total detak jantung
        
    Example:
        beats = calculate_heartbeats(1000000)
        print(f"{beats:,} kali detak jantung")
        # Output: 72,000,000 kali detak jantung
    """
    
    # Perkalian integer × integer = integer
    # total_minutes adalah int, AVERAGE_HEART_RATE_BPM juga int
    # Hasil perkalian adalah int
    total_heartbeats = total_minutes * AVERAGE_HEART_RATE_BPM
    
    # Return hasil sebagai integer
    # Integer bisa sangat besar di Python (tidak ada limit seperti di bahasa lain)
    return total_heartbeats


def calculate_breaths(total_minutes):
    """
    Fungsi untuk menghitung estimasi total napas sejak lahir.
    
    Rumus: Total napas = Total menit × Napas per menit
    
    Args:
        total_minutes (int): Total menit hidup
        
    Returns:
        int: Estimasi total napas
        
    Example:
        breaths = calculate_breaths(1000000)
        print(f"{breaths:,} kali napas")
        # Output: 16,000,000 kali napas
    """
    
    # Perkalian integer × integer = integer
    # Menghitung total napas berdasarkan rata-rata pernapasan per menit
    total_breaths = total_minutes * AVERAGE_BREATHING_RATE_PER_MINUTE
    
    # Return hasil sebagai integer
    return total_breaths


def calculate_sleep_hours(total_days):
    """
    Fungsi untuk menghitung estimasi total jam tidur sejak lahir.
    
    Rumus: Total jam tidur = Total hari × Jam tidur per hari
    
    Args:
        total_days (int): Total hari hidup
        
    Returns:
        int: Estimasi total jam tidur
        
    Example:
        sleep = calculate_sleep_hours(9500)
        print(f"{sleep:,} jam tidur")
        # Output: 76,000 jam tidur
    """
    
    # Perkalian integer × integer = integer
    # Menghitung total jam tidur berdasarkan rata-rata tidur 8 jam per hari
    total_sleep_hours = total_days * AVERAGE_SLEEP_HOURS_PER_DAY
    
    # Return hasil sebagai integer
    return total_sleep_hours


def calculate_total_steps(total_days):
    """
    Fungsi untuk menghitung estimasi total langkah kaki sejak bisa berjalan.
    
    Asumsi: Anak mulai berjalan umur 1 tahun
    Rumus: Total langkah = (Total hari - 365) × Langkah per hari
    
    Args:
        total_days (int): Total hari hidup
        
    Returns:
        int: Estimasi total langkah, atau 0 jika belum bisa berjalan
        
    Example:
        steps = calculate_total_steps(9500)
        print(f"{steps:,} langkah")
    """
    
    # Asumsi: Anak mulai berjalan setelah 365 hari (1 tahun)
    # Kita kurangi 365 hari dari total hari hidup
    days_walking = total_days - 365
    
    # Check apakah sudah bisa berjalan (umur > 1 tahun)
    # Jika total_days < 365, berarti belum 1 tahun, belum bisa jalan
    if days_walking < 0:
        # Return 0 jika belum bisa berjalan
        return 0
    
    # Hitung total langkah: hari berjalan × langkah per hari
    # Perkalian integer × integer = integer
    total_steps = days_walking * RECOMMENDED_STEPS_PER_DAY
    
    # Return hasil sebagai integer
    return total_steps


def calculate_percentage_sleeping(total_days):
    """
    Fungsi untuk menghitung persentase hidup yang dihabiskan untuk tidur.
    
    Dengan asumsi tidur 8 jam per hari:
    Persentase tidur = (8/24) × 100 = 33.33%
    
    Args:
        total_days (int): Total hari hidup
        
    Returns:
        float: Persentase waktu tidur (0-100)
        
    Example:
        pct = calculate_percentage_sleeping(9500)
        print(f"{pct:.2f}%")  # 33.33%
    """
    
    # Hitung total jam hidup
    # Perkalian integer × integer = integer
    total_hours = total_days * 24
    
    # Hitung total jam tidur
    # Perkalian integer × integer = integer
    total_sleep = total_days * AVERAGE_SLEEP_HOURS_PER_DAY
    
    # Hitung persentase
    # total_sleep dan total_hours adalah integer
    # Pembagian integer / integer di Python 3 menghasilkan float
    # Contoh: 10 / 3 = 3.3333333333333335
    percentage = (total_sleep / total_hours) * 100
    
    # Return hasil sebagai float
    # Float adalah bilangan desimal
    return percentage


def calculate_awake_hours(total_days):
    """
    Fungsi untuk menghitung total jam dalam keadaan terjaga (tidak tidur).
    
    Rumus: Jam terjaga = Total jam - Jam tidur
    
    Args:
        total_days (int): Total hari hidup
        
    Returns:
        int: Total jam terjaga
        
    Example:
        awake = calculate_awake_hours(9500)
        print(f"{awake:,} jam terjaga")
    """
    
    # Hitung total jam hidup
    # 1 hari = 24 jam
    total_hours = total_days * 24
    
    # Hitung total jam tidur
    total_sleep = calculate_sleep_hours(total_days)
    
    # Hitung jam terjaga: total jam - jam tidur
    # Pengurangan integer - integer = integer
    awake_hours = total_hours - total_sleep
    
    # Return hasil sebagai integer
    return awake_hours


def calculate_health_statistics(total_days, total_minutes):
    """
    Fungsi orchestrator untuk menghitung semua statistik kesehatan.
    
    Fungsi ini mengumpulkan hasil dari berbagai fungsi perhitungan
    dan menyimpannya dalam satu dictionary untuk kemudahan akses.
    
    Args:
        total_days (int): Total hari hidup
        total_minutes (int): Total menit hidup
        
    Returns:
        dict: Dictionary berisi semua statistik kesehatan dengan key:
            - "heartbeats": Total detak jantung (int)
            - "breaths": Total napas (int)
            - "sleep_hours": Total jam tidur (int)
            - "awake_hours": Total jam terjaga (int)
            - "sleep_percentage": Persentase waktu tidur (float)
            - "total_steps": Total langkah kaki (int)
            
    Example:
        stats = calculate_health_statistics(9500, 13680000)
        print(f"Total detak jantung: {stats['heartbeats']:,}")
        print(f"Persentase tidur: {stats['sleep_percentage']:.2f}%")
    """
    
    # Hitung semua statistik menggunakan fungsi-fungsi yang sudah dibuat
    # Setiap fungsi return tipe data yang spesifik (int atau float)
    
    # Calculate heartbeats - return int
    heartbeats = calculate_heartbeats(total_minutes)
    
    # Calculate breaths - return int
    breaths = calculate_breaths(total_minutes)
    
    # Calculate sleep hours - return int
    sleep_hours = calculate_sleep_hours(total_days)
    
    # Calculate awake hours - return int
    awake_hours = calculate_awake_hours(total_days)
    
    # Calculate sleep percentage - return float
    sleep_percentage = calculate_percentage_sleeping(total_days)
    
    # Calculate total steps - return int
    total_steps = calculate_total_steps(total_days)
    
    # Buat dictionary untuk menyimpan semua hasil
    # Dictionary memudahkan akses data dengan key yang deskriptif
    # Key adalah string, value bisa int atau float
    statistics = {
        "heartbeats": heartbeats,              # int
        "breaths": breaths,                    # int
        "sleep_hours": sleep_hours,            # int
        "awake_hours": awake_hours,            # int
        "sleep_percentage": sleep_percentage,  # float
        "total_steps": total_steps,            # int
    }
    
    # Return dictionary berisi semua statistik
    return statistics


# Testing modul jika file dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul health_stats ===")
    print()
    
    # Test dengan contoh data
    # Misalkan seseorang sudah hidup 9500 hari (sekitar 26 tahun)
    test_days = 9500
    test_minutes = test_days * 24 * 60  # Convert hari ke menit
    
    print(f"Test dengan {test_days:,} hari hidup ({test_minutes:,} menit)")
    print()
    
    # Test individual functions
    print("Test fungsi individual:")
    heartbeats = calculate_heartbeats(test_minutes)
    print(f"Total detak jantung: {heartbeats:,} kali")
    
    breaths = calculate_breaths(test_minutes)
    print(f"Total napas: {breaths:,} kali")
    
    sleep_hours = calculate_sleep_hours(test_days)
    print(f"Total jam tidur: {sleep_hours:,} jam")
    
    awake_hours = calculate_awake_hours(test_days)
    print(f"Total jam terjaga: {awake_hours:,} jam")
    
    sleep_pct = calculate_percentage_sleeping(test_days)
    print(f"Persentase tidur: {sleep_pct:.2f}%")
    
    steps = calculate_total_steps(test_days)
    print(f"Total langkah kaki: {steps:,} langkah")
    print()
    
    # Test orchestrator function
    print("Test calculate_health_statistics():")
    stats = calculate_health_statistics(test_days, test_minutes)
    print("Semua statistik:")
    for key, value in stats.items():
        # Check apakah value adalah float untuk formatting yang tepat
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value:,}")