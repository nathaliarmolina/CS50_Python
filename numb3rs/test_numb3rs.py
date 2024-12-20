from numb3rs import validate

def test_validate():
    assert validate("147.207.10.25") == True
    assert validate("358.207.10.25") == False
    assert validate("358") == False
    assert validate("358.20") == False
    assert validate("358.207.10") == False
    assert validate("255.255.255.255") == True

def test_out_of_range():
    assert validate("358.207.10.25.100") == False
    assert validate("358.207") == False

def test_numbers():

    assert validate("255.255.255.255.255") == False
    assert validate("1.1.1.555") == False
    assert validate("1.1.555.1") == False
    assert validate("1.555.1.1") == False
    assert validate("555.1.1.1") == False
