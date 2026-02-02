from utils import validate_not_empty, capitalize_first

def get_text_input(prompt: str, allow_empty: bool = False) -> str:
    while True:
        user_input = input(f"  {prompt}: ").strip()
        
        if allow_empty or validate_not_empty(user_input):
            return user_input
        else:
            print("  ⚠️  Input tidak boleh kosong! Silakan coba lagi.\n")

def get_choice(options: list, prompt: str = "Pilih") -> str:
    print(f"\n{prompt}:")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option.capitalize()}")