def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text: str) -> None:
    border = "=" * 50
    print(f"\n{border}")
    print(f"  {text.upper()}")
    print(f"{border}\n")


def print_separator() -> None:
    print("-" * 50)


def validate_not_empty(text: str) -> bool:
    return len(text.strip()) > 0


def capitalize_first(text: str) -> str:
    return text.strip().capitalize()


def format_list(items: list, conjunction: str = "dan") -> str:
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"
    else:
        return f"{', '.join(items[:-1])}, {conjunction} {items[-1]}"