import pytest
from working import convert


def test_convert():
    assert convert("11:30 PM to 8:50 AM") == "23:30 to 08:50"
    assert convert("10:00 AM to 5:00 PM") == "10:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
