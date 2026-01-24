"""
main.py - Entry Point CalcuAge Application

CalcuAge adalah aplikasi kalkulator umur yang menghitung:
- Umur dalam berbagai satuan waktu (tahun, hari, jam, menit, detik)
- Statistik kesehatan menarik (detak jantung, napas, tidur, langkah)
- Fun facts berdasarkan umur

Aplikasi ini mendemonstrasikan:
1. Modular programming - code terorganisir dalam modul-modul terpisah
2. Type system - penggunaan int, float, string, boolean, date
3. Type conversion - convert antar tipe data
4. Input validation - memastikan input user valid
5. Error handling - handle error dengan graceful
6. Separation of concerns - logic terpisah dari presentation

File ini adalah orchestrator yang mengoordinasikan semua modul.
"""

# Import semua fungsi yang dibutuhkan dari modul-modul yang sudah kita buat
# Setiap import statement membawa fungsi spesifik yang akan digunakan

# Dari input_handler: fungsi untuk handle input user
from input_handler import get_birth_date_input, confirm_birth_date, get_yes_no_input

# Dari age_calculator: fungsi untuk perhitungan umur
from age_calculator import calculate_age_breakdown, calculate_months_and_days

# Dari health_stats: fungsi untuk perhitungan statistik kesehatan
from health_stats import calculate_health_statistics

# Dari display: fungsi untuk menampilkan hasil
from display import (
    display_welcome_screen,
    display_age_breakdown,
    display_detailed_age,
    display_health_statistics,
    display_fun_facts,
    display_goodbye_message,
    print_separator,
)


def get_valid_birth_date():
    """
    Fungsi untuk mendapatkan tanggal lahir yang valid dari user.
    
    Fungsi ini akan loop sampai user memberikan tanggal lahir yang valid
    DAN user mengkonfirmasi bahwa tanggal tersebut benar.
    
    Returns:
        date: Object date tanggal lahir yang sudah dikonfirmasi
        
    Flow:
        1. Minta user input tanggal lahir
        2. Minta konfirmasi apakah tanggal benar
        3. Jika tidak, ulangi dari step 1
        4. Jika ya, return tanggal lahir
    """
    
    # Loop sampai mendapat tanggal lahir yang dikonfirmasi
    # while True = infinite loop, akan berhenti saat ada 'return'
    while True:
        # Minta user input tanggal lahir
        # get_birth_date_input() sudah handle semua validasi:
        # - Input harus integer
        # - Range tahun, bulan, hari valid
        # - Kombinasi tanggal valid (tidak ada Feb 31, dll)
        # - Tanggal tidak di masa depan
        birth_date = get_birth_date_input()
        
        # Minta user confirm tanggal lahir
        # confirm_birth_date() return True jika user confirm, False jika tidak
        # Ini adalah good UX practice untuk memastikan data penting benar
        confirmed = confirm_birth_date(birth_date)
        
        # Check hasil konfirmasi
        if confirmed:
            # Jika user confirm, tanggal lahir sudah benar
            # Return tanggal lahir dan keluar dari loop
            return birth_date
        else:
            # Jika user tidak confirm, ulangi proses input
            # Print message untuk feedback ke user
            print("\n🔄 Baik, mari input ulang tanggal lahir.")
            print()
            # Loop akan mengulang otomatis


def calculate_all_statistics(birth_date):
    """
    Fungsi untuk menghitung semua statistik umur dan kesehatan.
    
    Fungsi ini adalah orchestrator yang memanggil berbagai fungsi perhitungan
    dan mengumpulkan semua hasilnya.
    
    Args:
        birth_date (date): Object date tanggal lahir
        
    Returns:
        tuple: (breakdown, detailed, health_stats)
            - breakdown (dict): Breakdown umur dalam berbagai satuan
            - detailed (dict): Umur detail dalam tahun-bulan-hari
            - health_stats (dict): Statistik kesehatan
            
    Note:
        Return multiple values dengan tuple adalah pattern umum di Python
        Caller bisa unpack: breakdown, detailed, stats = calculate_all_statistics(date)
    """
    
    # Hitung breakdown umur (tahun, hari, jam, menit, detik)
    # calculate_age_breakdown() return dictionary dengan semua informasi umur
    breakdown = calculate_age_breakdown(birth_date)
    
    # Hitung umur detail (X tahun, Y bulan, Z hari)
    # calculate_months_and_days() return dictionary dengan years, months, days
    detailed = calculate_months_and_days(birth_date)
    
    # Hitung statistik kesehatan
    # Kita perlu total_days dan total_minutes dari breakdown
    # Dictionary access dengan [key]
    total_days = breakdown["total_days"]
    total_minutes = breakdown["total_minutes"]
    
    # calculate_health_statistics() return dictionary dengan semua statistik kesehatan
    health_stats = calculate_health_statistics(total_days, total_minutes)
    
    # Return tuple dengan 3 dictionary
    # Tuple dibuat dengan tanda kurung () atau cukup comma-separated values
    # Python automatically pack multiple return values into tuple
    return breakdown, detailed, health_stats


def display_all_results(breakdown, detailed, health_stats):
    """
    Fungsi untuk menampilkan semua hasil perhitungan.
    
    Fungsi ini mengoordinasikan berbagai display function
    untuk menampilkan hasil dalam format yang menarik dan terstruktur.
    
    Args:
        breakdown (dict): Breakdown umur dalam berbagai satuan
        detailed (dict): Umur detail dalam tahun-bulan-hari
        health_stats (dict): Statistik kesehatan
        
    Side Effect:
        Mencetak semua hasil ke terminal
    """
    
    # Print separator untuk visual separation
    print()
    print_separator("=", 60)
    print()
    
    # Display age breakdown
    # Fungsi ini menampilkan umur dalam tahun, hari, jam, menit, detik
    display_age_breakdown(breakdown)
    
    # Display detailed age
    # Fungsi ini menampilkan umur dalam format "X tahun, Y bulan, Z hari"
    display_detailed_age(detailed)
    
    # Display health statistics
    # Fungsi ini menampilkan statistik kesehatan (detak jantung, napas, tidur, dll)
    display_health_statistics(health_stats)
    
    # Display fun facts
    # Fungsi ini menampilkan fakta-fakta menarik berdasarkan umur
    display_fun_facts(breakdown, health_stats)


def run_calcuage():
    """
    Fungsi utama yang menjalankan aplikasi CalcuAge.
    
    Fungsi ini adalah core flow aplikasi yang:
    1. Menampilkan welcome screen
    2. Mendapatkan tanggal lahir dari user
    3. Menghitung semua statistik
    4. Menampilkan hasil
    5. Menampilkan goodbye message
    6. Tanya apakah user mau hitung lagi untuk orang lain
    
    Flow ini mengikuti pattern umum aplikasi CLI:
    - Setup (welcome)
    - Input (get data)
    - Process (calculate)
    - Output (display results)
    - Cleanup (goodbye)
    - Loop option (calculate again?)
    """
    
    # Display welcome screen
    # Ini memberikan user context tentang aplikasi
    display_welcome_screen()
    
    # Main application loop
    # Loop ini memungkinkan user menghitung untuk multiple orang
    # tanpa restart aplikasi
    while True:
        # STEP 1: Get valid birth date from user
        # Fungsi ini akan loop sampai dapat tanggal lahir yang valid dan confirmed
        birth_date = get_valid_birth_date()
        
        # STEP 2: Calculate all statistics
        # Fungsi ini return 3 dictionary: breakdown, detailed, health_stats
        # Kita unpack tuple hasil return ke 3 variabel terpisah
        # Python feature: multiple assignment / tuple unpacking
        breakdown, detailed, health_stats = calculate_all_statistics(birth_date)
        
        # STEP 3: Display all results
        # Fungsi ini menampilkan semua hasil dengan format yang menarik
        display_all_results(breakdown, detailed, health_stats)
        
        # STEP 4: Ask if user wants to calculate for another person
        # get_yes_no_input() return True untuk yes, False untuk no
        print()
        want_continue = get_yes_no_input(
            "Apakah Anda ingin menghitung untuk orang lain? (y/n): "
        )
        
        # Check user response
        if want_continue:
            # Jika user mau lanjut, print message dan loop akan mengulang
            print("\n" + "=" * 60)
            print("Baik, mari hitung untuk orang lain! 🔄".center(60))
            print("=" * 60)
            print()
            # Loop continues ke awal while
        else:
            # Jika user tidak mau lanjut, keluar dari loop
            # break statement menghentikan loop
            break
    
    # STEP 5: Display goodbye message
    # Ini dijalankan setelah user memilih untuk tidak lanjut (keluar dari loop)
    display_goodbye_message()


def main():
    """
    Main function - Entry point ketika script dijalankan.
    
    Fungsi ini adalah best practice untuk Python application.
    Kita wrap main logic dalam function agar:
    1. Bisa di-import tanpa auto-execute
    2. Bisa di-test dengan lebih mudah
    3. Bisa handle error di level tertinggi
    
    Pattern ini mengikuti convention yang digunakan di banyak
    framework dan library Python profesional.
    """
    
    # Try-except untuk handle unexpected errors
    # Di production code, error handling sangat penting
    try:
        # Jalankan aplikasi utama
        run_calcuage()
        
    except KeyboardInterrupt:
        # KeyboardInterrupt terjadi saat user tekan Ctrl+C
        # Ini adalah cara graceful untuk handle force quit
        print("\n\n" + "=" * 60)
        print("Program dihentikan oleh user.".center(60))
        print("Terima kasih sudah menggunakan CalcuAge! 👋".center(60))
        print("=" * 60)
        print()
        
    except Exception as e:
        # Catch-all untuk error lain yang tidak terduga
        # Dalam production, kita mungkin log error ini
        # Dan tampilkan user-friendly message
        print("\n\n" + "=" * 60)
        print("Terjadi error yang tidak terduga:".center(60))
        print(f"{str(e)}".center(60))
        print()
        print("Mohon maaf atas ketidaknyamanannya.".center(60))
        print("Silakan coba restart aplikasi.".center(60))
        print("=" * 60)
        print()


# Special Python idiom untuk detect apakah file dijalankan langsung
# __name__ adalah special variable yang ada di setiap Python file
# Nilainya "__main__" jika file dijalankan langsung
# Nilainya nama module jika file di-import
#
# Pattern ini memungkinkan file berfungsi dual-purpose:
# 1. Sebagai executable script: python main.py
# 2. Sebagai importable module: from main import run_calcuage
#
# Best practice di Python untuk semua executable scripts
if __name__ == "__main__":
    # Block ini hanya dijalankan jika file dirun langsung
    # Tidak dijalankan jika file di-import di file lain
    
    # Call main function untuk start aplikasi
    # Dengan memisahkan main() dari if __name__,
    # kita bisa test main() secara terpisah jika diperlukan
    main()
    
    # Notes untuk developer:
    # - Aplikasi ini bisa di-extend dengan fitur lain:
    #   * Export hasil ke file (TXT, PDF, CSV)
    #   * Compare umur dengan orang lain
    #   * Visualisasi dengan chart/graph
    #   * GUI dengan Tkinter atau PyQt
    #   * Web version dengan Flask atau FastAPI
    # - Code structure sudah modular, mudah untuk ditambahkan fitur baru
    # - Setiap modul bisa di-test independen
    # - Ikuti same pattern untuk konsistensi