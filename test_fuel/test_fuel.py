from fuel import convert, gauge
import pytest



def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50




def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("7/0")

def invalid_fraction():
    with pytest.raises(ValueError):
        convert("4/2")

def test_first_letter():
    with pytest.raises(ValueError):
        convert("M/7")


def test_second_letter():
    with pytest.raises(ValueError):
        convert("4/C")



