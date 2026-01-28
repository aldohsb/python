def get_bill_amount():
    """Meminta input total bill dari user dengan validasi"""
    while True:
        try:
            bill = input("Masukkan total bill (Rp): ")
            bill = float(bill)
            
            if bill <= 0:
                print("❌ Total bill harus lebih dari 0!")
                continue
            
            return bill
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka yang benar.")


def get_tip_percentage(suggestions):
    """Meminta input persentase tip dari user"""
    print(f"\nPilih persentase tip:")
    for i, percent in enumerate(suggestions, 1):
        print(f"{i}. {percent}%")
    print(f"{len(suggestions) + 1}. Custom")
    
    while True:
        try:
            choice = input("\nPilihan Anda (1-4): ")
            choice = int(choice)
            
            if 1 <= choice <= len(suggestions):
                return suggestions[choice - 1]
            elif choice == len(suggestions) + 1:
                return get_custom_tip()
            else:
                print("❌ Pilihan tidak valid!")
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka.")


def get_custom_tip():
    """Meminta input custom persentase tip"""
    while True:
        try:
            tip = input("Masukkan persentase tip custom (%): ")
            tip = float(tip)
            
            if tip < 0:
                print("❌ Persentase tidak boleh negatif!")
                continue
            
            return tip
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka yang benar.")


def get_number_of_people():
    """Meminta input jumlah orang untuk split bill"""
    while True:
        try:
            people = input("\nJumlah orang untuk split bill: ")
            people = int(people)
            
            if people <= 0:
                print("❌ Jumlah orang harus lebih dari 0!")
                continue
            
            return people
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka bulat.")


def ask_split_bill():
    """Menanyakan apakah user ingin split bill"""
    while True:
        answer = input("\nApakah ingin split bill? (y/n): ").lower()
        if answer in ['y', 'yes', 'ya']:
            return True
        elif answer in ['n', 'no', 'tidak']:
            return False
        else:
            print("❌ Input tidak valid! Ketik 'y' atau 'n'.")