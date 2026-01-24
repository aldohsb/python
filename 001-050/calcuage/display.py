"""
Modul display.py
Modul ini bertanggung jawab untuk semua formatting dan display output ke user.

Separation of concerns: Logic terpisah dari presentation.
- Business logic ada di age_calculator dan health_stats
- Presentation logic ada di modul ini

Modul ini demonstrate:
- String formatting dengan f-strings
- Number formatting untuk readability (:, format)
- Float formatting untuk presisi (.2f format)
- Layout design dengan ASCII art dan spacing
"""


def print_header(title, width=60):
    """
    Fungsi untuk print header dengan border yang menarik.
    
    Args:
        title (str): Judul yang akan ditampilkan
        width (int): Lebar total header (default 60)
        
    Side Effect:
        Mencetak header ke terminal
        
    Example:
        print_header("CALCUAGE")
        # Output:
        # ============================================================
        #                          CALCUAGE
        # ============================================================
    """
    
    # Print border atas
    # "=" * width akan menghasilkan string "=" sebanyak width kali
    print("=" * width)
    
    # Print title di tengah
    # .center(width) membuat string di tengah dengan total width tertentu
    # Padding otomatis ditambahkan di kiri dan kanan
    print(title.center(width))
    
    # Print border bawah
    print("=" * width)


def print_subheader(title, width=60):
    """
    Fungsi untuk print subheader dengan border yang lebih simple.
    
    Args:
        title (str): Subjudul yang akan ditampilkan
        width (int): Lebar total subheader (default 60)
        
    Side Effect:
        Mencetak subheader ke terminal
    """
    
    # Print line kosong untuk spacing
    print()
    
    # Print border dengan karakter "-" (lebih subtle dari "=")
    print("-" * width)
    
    # Print title di tengah
    print(title.center(width))
    
    # Print border
    print("-" * width)
    
    # Print line kosong
    print()


def print_separator(char="=", width=60):
    """
    Fungsi utility untuk print separator line.
    
    Args:
        char (str): Karakter untuk separator (default "=")
        width (int): Lebar separator (default 60)
        
    Side Effect:
        Mencetak separator ke terminal
    """
    
    # Print separator character sebanyak width kali
    print(char * width)


def format_large_number(number):
    """
    Fungsi untuk format angka besar dengan separator ribuan.
    
    Python punya built-in formatting untuk angka:
    {:,} akan menambahkan koma sebagai thousand separator
    
    Args:
        number (int): Angka yang akan diformat
        
    Returns:
        str: String angka dengan format ribuan
        
    Example:
        formatted = format_large_number(1234567)
        print(formatted)  # "1,234,567"
    """
    
    # Format angka dengan koma sebagai thousand separator
    # f"{number:,}" sama dengan f-string dengan format spec :,
    # Contoh: 1234567 -> "1,234,567"
    # Contoh: 1000 -> "1,000"
    return f"{number:,}"


def display_welcome_screen():
    """
    Fungsi untuk menampilkan welcome screen aplikasi.
    
    Welcome screen membuat aplikasi terlihat lebih profesional
    dan memberikan user context tentang apa yang akan dilakukan.
    
    Side Effect:
        Mencetak welcome screen ke terminal
    """
    
    # Print beberapa line kosong untuk clear screen effect
    print("\n" * 2)
    
    # Print header utama dengan ASCII art
    print_header("🎂 CALCUAGE - KALKULATOR UMUR 🎂")
    
    # Print line kosong
    print()
    
    # Print deskripsi aplikasi
    # Triple-quoted string untuk multiline text
    # Kita bisa tulis teks dalam beberapa baris dengan natural
    description = """
    Selamat datang di CalcuAge!
    
    Aplikasi ini akan menghitung:
    • Umur Anda dalam berbagai satuan waktu
    • Total hari, jam, menit, detik hidup
    • Estimasi statistik kesehatan yang menarik
    
    Mari kita mulai! 🚀
    """
    
    # Print deskripsi
    # strip() untuk hapus whitespace di awal dan akhir
    print(description.strip())
    
    # Print line kosong
    print()
    
    # Print separator
    print_separator()


def display_age_breakdown(breakdown):
    """
    Fungsi untuk menampilkan breakdown umur dalam berbagai satuan.
    
    Args:
        breakdown (dict): Dictionary hasil dari calculate_age_breakdown()
            dengan key: years, total_days, total_hours, total_minutes, total_seconds
            
    Side Effect:
        Mencetak breakdown umur ke terminal
        
    Example:
        breakdown = {
            "years": 25,
            "total_days": 9500,
            "total_hours": 228000,
            ...
        }
        display_age_breakdown(breakdown)
    """
    
    # Print subheader
    print_subheader("⏰ UMUR ANDA DALAM BERBAGAI SATUAN")
    
    # Extract data dari dictionary
    # Dictionary access dengan [key] akan get value
    years = breakdown["years"]
    total_days = breakdown["total_days"]
    total_hours = breakdown["total_hours"]
    total_minutes = breakdown["total_minutes"]
    total_seconds = breakdown["total_seconds"]
    
    # Print umur dalam tahun (paling common)
    # f-string dengan format :,} untuk thousand separator
    print(f"  🎂 Umur Anda: {years} tahun")
    print()
    
    # Print breakdown dalam satuan lain
    # Kita group output untuk visual yang lebih baik
    print("  Atau sama dengan:")
    print(f"    • {format_large_number(total_days)} hari")
    print(f"    • {format_large_number(total_hours)} jam")
    print(f"    • {format_large_number(total_minutes)} menit")
    print(f"    • {format_large_number(total_seconds)} detik")
    
    # Print line kosong untuk spacing
    print()


def display_detailed_age(detailed):
    """
    Fungsi untuk menampilkan umur detail dalam format "X tahun, Y bulan, Z hari".
    
    Args:
        detailed (dict): Dictionary hasil dari calculate_months_and_days()
            dengan key: years, months, days
            
    Side Effect:
        Mencetak umur detail ke terminal
        
    Example:
        detailed = {"years": 25, "months": 8, "days": 7}
        display_detailed_age(detailed)
        # Output: "  📅 Umur detail: 25 tahun, 8 bulan, 7 hari"
    """
    
    # Extract data dari dictionary
    years = detailed["years"]
    months = detailed["months"]
    days = detailed["days"]
    
    # Print umur detail
    # f-string memudahkan embed multiple variables
    print(f"  📅 Umur detail: {years} tahun, {months} bulan, {days} hari")
    print()


def display_health_statistics(stats):
    """
    Fungsi untuk menampilkan statistik kesehatan yang menarik.
    
    Args:
        stats (dict): Dictionary hasil dari calculate_health_statistics()
            dengan key: heartbeats, breaths, sleep_hours, awake_hours,
            sleep_percentage, total_steps
            
    Side Effect:
        Mencetak statistik kesehatan ke terminal
        
    Example:
        stats = {
            "heartbeats": 984960000,
            "breaths": 218880000,
            ...
        }
        display_health_statistics(stats)
    """
    
    # Print subheader
    print_subheader("💪 STATISTIK KESEHATAN MENARIK")
    
    # Extract data dari dictionary
    heartbeats = stats["heartbeats"]
    breaths = stats["breaths"]
    sleep_hours = stats["sleep_hours"]
    awake_hours = stats["awake_hours"]
    sleep_percentage = stats["sleep_percentage"]
    total_steps = stats["total_steps"]
    
    # Display heartbeats
    # Emoji 💓 membuat output lebih menarik dan friendly
    print(f"  💓 Estimasi total detak jantung:")
    print(f"     {format_large_number(heartbeats)} kali detak")
    print(f"     (dengan asumsi rata-rata 72 detak/menit)")
    print()
    
    # Display breaths
    print(f"  🌬️  Estimasi total napas:")
    print(f"     {format_large_number(breaths)} kali napas")
    print(f"     (dengan asumsi rata-rata 16 napas/menit)")
    print()
    
    # Display sleep statistics
    print(f"  😴 Statistik tidur:")
    print(f"     Total jam tidur: {format_large_number(sleep_hours)} jam")
    print(f"     Total jam terjaga: {format_large_number(awake_hours)} jam")
    # Format float dengan 2 decimal places menggunakan :.2f
    # .2f = float dengan 2 digit di belakang koma
    print(f"     Persentase waktu tidur: {sleep_percentage:.2f}%")
    print(f"     (dengan asumsi tidur 8 jam/hari)")
    print()
    
    # Display steps
    # Check jika total_steps > 0 (artinya sudah bisa jalan)
    if total_steps > 0:
        print(f"  👣 Estimasi total langkah kaki:")
        print(f"     {format_large_number(total_steps)} langkah")
        print(f"     (dengan asumsi 10,000 langkah/hari sejak umur 1 tahun)")
    else:
        # Jika total_steps = 0, berarti belum bisa jalan (umur < 1 tahun)
        print(f"  👣 Belum bisa berjalan (umur < 1 tahun)")
    
    # Print line kosong
    print()


def display_fun_facts(breakdown, stats):
    """
    Fungsi untuk menampilkan fakta-fakta menarik berdasarkan umur.
    
    Args:
        breakdown (dict): Dictionary breakdown umur
        stats (dict): Dictionary statistik kesehatan
        
    Side Effect:
        Mencetak fun facts ke terminal
    """
    
    # Print subheader
    print_subheader("🎉 FAKTA MENARIK")
    
    # Extract data yang kita butuhkan
    years = breakdown["years"]
    total_days = breakdown["total_days"]
    heartbeats = stats["heartbeats"]
    
    # Calculate beberapa fun facts
    
    # Berapa kali ulang tahun (umur = jumlah ulang tahun)
    print(f"  🎂 Anda sudah merayakan {years} kali ulang tahun!")
    print()
    
    # Berapa kali Hari Senin (asumsi 1/7 dari total hari)
    # Pembagian integer // untuk dapat hasil bulat
    # Kita pakai // agar hasilnya integer (bukan float)
    mondays = total_days // 7
    print(f"  📅 Anda sudah melewati sekitar {format_large_number(mondays)} hari Senin")
    print()
    
    # Jika umur >= 18, hitung berapa hari sejak dewasa
    if years >= 18:
        # Hitung hari sejak umur 18
        # 1 tahun ≈ 365.25 hari (accounting for leap years)
        # Convert ke int karena hari harus integer
        years_since_adult = years - 18
        days_since_adult = int(years_since_adult * 365.25)
        print(f"  🎓 Anda sudah dewasa selama {format_large_number(days_since_adult)} hari")
        print()
    
    # Berapa tahun dalam bentuk decimal yang presisi
    # Lebih akurat dari integer years
    # total_days / 365.25 memberikan tahun dalam decimal
    precise_years = total_days / 365.25
    print(f"  🔢 Umur presisi: {precise_years:.4f} tahun")
    # :.4f = float dengan 4 decimal places
    print()
    
    # Compare heartbeats dengan sesuatu yang familiar
    # 1 miliar = 1,000,000,000
    billions_of_beats = heartbeats / 1_000_000_000
    # Underscore dalam number literal untuk readability: 1_000_000_000 = 1000000000
    # Python 3.6+ feature
    print(f"  💗 Jantung Anda sudah berdetak {billions_of_beats:.2f} miliar kali!")
    print()


def display_goodbye_message():
    """
    Fungsi untuk menampilkan pesan penutup.
    
    Side Effect:
        Mencetak goodbye message ke terminal
    """
    
    # Print line kosong
    print()
    
    # Print separator
    print_separator()
    
    # Print goodbye message
    goodbye = """
    Terima kasih sudah menggunakan CalcuAge! 🎉
    
    Semoga informasi ini memberikan perspektif menarik
    tentang perjalanan hidup Anda.
    
    Setiap detik adalah berharga. Gunakan dengan bijak! ⏰
    
    Stay healthy and keep coding! 💻
    """
    
    # Print dengan centered alignment
    # Split by newline, center each line
    for line in goodbye.strip().split("\n"):
        print(line.center(60))
    
    # Print separator
    print()
    print_separator()
    print()


# Testing modul jika file dijalankan langsung
if __name__ == "__main__":
    print("=== Testing Modul display ===")
    print()
    
    # Test display_welcome_screen()
    display_welcome_screen()
    
    # Wait for enter
    input("Tekan Enter untuk lanjut testing...")
    
    # Test dengan sample data
    from datetime import date
    
    # Sample breakdown data
    sample_breakdown = {
        "years": 25,
        "total_days": 9500,
        "total_hours": 228000,
        "total_minutes": 13680000,
        "total_seconds": 820800000,
        "birth_date": date(2000, 5, 15),
        "current_date": date.today(),
    }
    
    # Sample detailed age
    sample_detailed = {
        "years": 25,
        "months": 8,
        "days": 7,
    }
    
    # Sample health stats
    sample_stats = {
        "heartbeats": 984960000,
        "breaths": 218880000,
        "sleep_hours": 76000,
        "awake_hours": 152000,
        "sleep_percentage": 33.33,
        "total_steps": 91350000,
    }
    
    # Test display functions
    display_age_breakdown(sample_breakdown)
    display_detailed_age(sample_detailed)
    display_health_statistics(sample_stats)
    display_fun_facts(sample_breakdown, sample_stats)
    display_goodbye_message()