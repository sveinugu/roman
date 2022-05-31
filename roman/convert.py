def decimal_to_roman(number: int) -> str:
    if number < 5:
        return 'I' * number
    elif number < 10:
        return 'V' + 'I' * (number - 5)
    else:
        return 'X' + 'I' * (number - 10)
