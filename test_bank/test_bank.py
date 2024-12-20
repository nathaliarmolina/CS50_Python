from bank import value

def test_value():
    assert value("hi") == 20
    assert value("hello") == 0
    assert value("olá") == 100
    assert value("batata") == 100
    assert value("Hello") == 0
    assert value("Hi") == 20