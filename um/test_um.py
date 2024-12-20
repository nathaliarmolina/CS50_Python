from um import count

def test_count():
    assert count("um dois três") == 1
    assert count("um dois um dois") == 2
    assert count("um dois um dois um") == 3
    assert count("um um um um") == 4
    assert count("um") == 1
    assert count("uma") == 0

def test_count_m():
    assert count("Um dois três") == 1
    assert count("Um dois Um dois") == 2
    assert count("Um dois Um dois Um") == 3
    assert count("Um Um Um Um") == 4

def test_count_x():
    assert count("Um dois três um") == 2
    assert count("Um dois um dois") == 2
    assert count("Um dois Um Um") == 3
    assert count("Um um Um um") == 4


