from calculator import (
    calculate_tip,
    calculate_total,
    split_bill,
    get_tip_suggestions
)
from input_handler import (
    get_bill_amount,
    get_tip_percentage,
    get_number_of_people,
    ask_split_bill
)
from formatter import (
    print_header,
    print_result,
    print_thank_you
)


def main():
    """Fungsi utama aplikasi TipMaster"""
    print_header()
    
    bill_amount = get_bill_amount()
    
    tip_suggestions = get_tip_suggestions()
    tip_percentage = get_tip_percentage(tip_suggestions)
    
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total = calculate_total(bill_amount, tip_amount)
    
    if ask_split_bill():
        num_people = get_number_of_people()
        per_person = split_bill(total, num_people)
        print_result(bill_amount, tip_percentage, tip_amount, total, per_person, num_people)
    else:
        print_result(bill_amount, tip_percentage, tip_amount, total)
    
    print_thank_you()


if __name__ == "__main__":
    main()