def format_currency(amount):
    """Format angka menjadi format Rupiah"""
    return f"Rp {amount:,.2f}"


def print_separator():
    """Cetak garis pemisah"""
    print("=" * 50)


def print_header():
    """Cetak header aplikasi"""
    print_separator()
    print("🍽️  TIPMASTER - KALKULATOR TIP RESTAURANT  🍽️")
    print_separator()


def print_result(bill, tip_percentage, tip_amount, total, per_person=None, num_people=None):
    """Cetak hasil perhitungan dengan format yang rapi"""
    print_separator()
    print("📊 RINCIAN PEMBAYARAN")
    print_separator()
    
    print(f"Total Bill        : {format_currency(bill)}")
    print(f"Tip ({tip_percentage}%)       : {format_currency(tip_amount)}")
    print("-" * 50)
    print(f"TOTAL             : {format_currency(total)}")
    
    if per_person is not None and num_people is not None:
        print_separator()
        print(f"Dibagi {num_people} orang")
        print(f"Per Orang         : {format_currency(per_person)}")
    
    print_separator()


def print_thank_you():
    """Cetak pesan terima kasih"""
    print("\n✅ Terima kasih telah menggunakan TipMaster!")
    print("Semoga hari Anda menyenangkan! 😊")