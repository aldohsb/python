"""
Module: validator.py
Deskripsi: Validasi input dari user (type checking dan logical validation)
Fungsi: Memastikan input valid sebelum diproses lebih lanjut
"""

# Import konstanta yang diperlukan
from .constants import (
    ABSOLUTE_ZERO_CELSIUS,
    ABSOLUTE_ZERO_FAHRENHEIT,
    ABSOLUTE_ZERO_KELVIN,
    ERROR_INVALID_NUMBER,
    ERROR_BELOW_ABSOLUTE_ZERO,
    ERROR_INVALID_SCALE
)


def validate_temperature_input(user_input: str) -> tuple[bool, float, str]:
    """
    Validasi input suhu dari user dan konversi ke float
    
    Args:
        user_input (str): Input string dari user
        
    Returns:
        tuple[bool, float, str]: (is_valid, converted_value, error_message)
        - is_valid: True jika valid, False jika tidak
        - converted_value: Nilai yang sudah dikonversi ke float (0.0 jika invalid)
        - error_message: Pesan error (string kosong jika valid)
        
    Contoh:
        >>> validate_temperature_input("25.5")
        (True, 25.5, "")
        
        >>> validate_temperature_input("abc")
        (False, 0.0, "❌ Input bukan angka yang valid!")
    """
    try:
        # Coba konversi string ke float
        # strip() menghilangkan spasi di awal/akhir
        temperature: float = float(user_input.strip())
        
        # Jika berhasil dikonversi, return True dengan nilai dan pesan kosong
        return True, temperature, ""
        
    except ValueError:
        # Jika gagal (misal input "abc"), return False dengan error message
        return False, 0.0, ERROR_INVALID_NUMBER


def validate_scale_input(user_input: str) -> tuple[bool, str, str]:
    """
    Validasi input skala suhu (C/F/K) dari user
    
    Args:
        user_input (str): Input skala dari user (misal "C", "c", "celsius")
        
    Returns:
        tuple[bool, str, str]: (is_valid, normalized_scale, error_message)
        - is_valid: True jika valid, False jika tidak
        - normalized_scale: Skala yang sudah dinormalisasi ("C", "F", atau "K")
        - error_message: Pesan error (string kosong jika valid)
        
    Contoh:
        >>> validate_scale_input("C")
        (True, "C", "")
        
        >>> validate_scale_input("celsius")
        (True, "C", "")
        
        >>> validate_scale_input("X")
        (False, "", "❌ Skala suhu tidak valid!")
    """
    # Normalisasi input: uppercase dan ambil karakter pertama
    # strip() menghilangkan spasi, upper() mengubah ke huruf besar
    normalized: str = user_input.strip().upper()
    
    # Jika user mengetik "CELSIUS", ambil hanya "C"
    if normalized in ["CELSIUS", "CEL"]:
        normalized = "C"
    elif normalized in ["FAHRENHEIT", "FAH"]:
        normalized = "F"
    elif normalized in ["KELVIN", "KEL"]:
        normalized = "K"
    else:
        # Ambil karakter pertama (untuk kasus user input "C" atau "c")
        normalized = normalized[0] if normalized else ""
    
    # Cek apakah termasuk skala yang valid
    if normalized in ["C", "F", "K"]:
        return True, normalized, ""
    else:
        return False, "", ERROR_INVALID_SCALE


def validate_absolute_zero(temperature: float, scale: str) -> tuple[bool, str]:
    """
    Validasi apakah suhu di atas absolute zero (secara fisika impossible)
    
    Args:
        temperature (float): Nilai suhu yang akan divalidasi
        scale (str): Skala suhu ("C", "F", atau "K")
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
        - is_valid: True jika di atas absolute zero, False jika tidak
        - error_message: Pesan error (string kosong jika valid)
        
    Penjelasan Absolute Zero:
        - Celsius: -273.15°C
        - Fahrenheit: -459.67°F
        - Kelvin: 0 K
        Suhu tidak bisa lebih rendah dari nilai ini (hukum termodinamika)
        
    Contoh:
        >>> validate_absolute_zero(-300, "C")
        (False, "❌ Suhu tidak bisa lebih rendah dari absolute zero!")
        
        >>> validate_absolute_zero(25, "C")
        (True, "")
    """
    # Dictionary untuk memetakan skala ke nilai absolute zero-nya
    absolute_zeros: dict[str, float] = {
        "C": ABSOLUTE_ZERO_CELSIUS,    # -273.15
        "F": ABSOLUTE_ZERO_FAHRENHEIT,  # -459.67
        "K": ABSOLUTE_ZERO_KELVIN       # 0.0
    }
    
    # Ambil nilai absolute zero untuk skala yang dipilih
    min_temperature: float = absolute_zeros[scale]
    
    # Cek apakah suhu lebih rendah dari absolute zero
    # Gunakan sedikit toleransi (0.01) untuk floating point precision
    if temperature < min_temperature - 0.01:
        return False, ERROR_BELOW_ABSOLUTE_ZERO
    
    return True, ""


def get_validated_input(prompt: str, validator_func) -> tuple[any, str]:
    """
    Generic function untuk mendapatkan input yang sudah tervalidasi
    
    Args:
        prompt (str): Pesan yang ditampilkan ke user
        validator_func: Fungsi validator yang akan digunakan
        
    Returns:
        tuple: Hasil dari fungsi validator
        
    Note:
        Ini adalah helper function untuk mengurangi code duplication
    """
    user_input: str = input(prompt)
    return validator_func(user_input)