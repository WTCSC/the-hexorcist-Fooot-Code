import hexorcist
import pytest

def test_base16_to_decimal():
    """
    Test converting a hexadecimal (base 16) string to a decimal integer.
    '1A4' in base 16 should equal 420 in decimal.
    """
    assert hexorcist.to_decimal("1A4", 16) == 420

def test_binary_to_decimal():
    """
    Test converting a binary (base 2) string to a decimal integer.
    '10101' in base 2 should equal 21 in decimal.
    """
    assert hexorcist.to_decimal("10101", 2) == 21

def test_base36_to_decimal():
    """
    Test converting a base 36 string to a decimal integer.
    '67' in base 36 should equal 223 in decimal.
    """
    assert hexorcist.to_decimal("67", 36) == 223

def test_from_decimal_to_base9():
    """
    Test converting a decimal integer to a base 9 string.
    453 in decimal should equal '553' in base 9.
    """
    assert hexorcist.from_decimal(453, 9) == "553"

def test_from_decimal_to_base2():
    """
    Test converting a decimal integer to a binary (base 2) string.
    67 in decimal should equal '1000011' in binary.
    """
    assert hexorcist.from_decimal(67, 2) == "1000011"

def test_from_decimal_to_base23():
    """
    Test converting a decimal integer to a base 23 string.
    93 in decimal should equal '41' in base 23.
    """
    assert hexorcist.from_decimal(93, 23) == "41"
