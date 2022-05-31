from roman import __version__
from roman import convert


def test_version():
    assert __version__ == '0.1.0'


def test_simple_numbers():
    assert convert.decimal_to_roman(1) == 'I'
    assert convert.decimal_to_roman(2) == 'II'
    assert convert.decimal_to_roman(3) == 'III'

    assert convert.decimal_to_roman(5) == 'V'
    assert convert.decimal_to_roman(6) == 'VI'
    assert convert.decimal_to_roman(7) == 'VII'
    assert convert.decimal_to_roman(8) == 'VIII'

    assert convert.decimal_to_roman(10) == 'X'
