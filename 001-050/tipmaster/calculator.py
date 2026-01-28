def calculate_tip(bill_amount, tip_percentage):
    """Menghitung jumlah tip berdasarkan total bill dan persentase"""
    tip_amount = bill_amount * (tip_percentage / 100)
    return tip_amount


def calculate_total(bill_amount, tip_amount):
    """Menghitung total yang harus dibayar (bill + tip)"""
    total = bill_amount + tip_amount
    return total


def split_bill(total_amount, number_of_people):
    """Membagi total bill untuk beberapa orang"""
    if number_of_people <= 0:
        return 0
    
    per_person = total_amount / number_of_people
    return per_person


def get_tip_suggestions():
    """Mengembalikan daftar persentase tip yang umum digunakan"""
    return [10, 15, 20]