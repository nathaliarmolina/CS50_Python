from plates import is_valid

def test_len():
    assert is_valid("OO") == True
    assert is_valid("A") == False
    assert is_valid("ASDFGHJKL") == False

def test_validate_zero():
    assert is_valid("ABC10") == True
    assert is_valid("ABC01") == False

def test_alphanumeric():
    assert is_valid("CAT123") == True
    assert is_valid("CAT_22") == False

def test_is_valid_2_digits():
    assert is_valid("YU") == True
    assert is_valid("1G") == False

def test_is_valid_3_digits():
    assert is_valid("AMO") == True
    assert is_valid("NA7") == True
    assert is_valid("1G2") == False
    assert is_valid("45Y") == False

def test_is_valid_4_digits():
    assert is_valid("LOV3") == True
    assert is_valid("AA72") == True
    assert is_valid("12G2") == False
    assert is_valid("1224") == False

def test_is_valid_5_digits():
    assert is_valid("MARIA") == True
    assert is_valid("MOR79") == True
    assert is_valid("4Q12T") == False
    assert is_valid("WG2T2") == False

def test_is_valid_6_digits():
    assert is_valid("VIVIAN") == True
    assert is_valid("4U69TT") == False
    assert is_valid("AAG2T2") == False