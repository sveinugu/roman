decimal_to_roman_letter = {1: 'I', 5: 'V', 10: 'X'}


def decimal_to_roman(number: int) -> str:
    ret = ''

    for i in reversed(sorted(decimal_to_roman_letter.keys())):
        if number >= i:
            ret += decimal_to_roman_letter[i] * (number // i)
            number -= i

    return ret
