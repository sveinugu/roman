from collections import namedtuple

DecimalRange = namedtuple('DecimalRange', ('min', 'max'))

roman_letter_to_decimal_range = {
    'I': DecimalRange(1, 5), 'V': DecimalRange(5, 10), 'X': DecimalRange(10, 50)
}


def decimal_to_roman(number: int) -> str:
    for roman_letter, decimal_range in roman_letter_to_decimal_range.items():
        if number < decimal_range.max:
            return roman_letter + 'I' * (number - decimal_range.min)
