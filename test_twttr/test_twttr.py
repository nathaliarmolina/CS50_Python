from twttr import shorten

def test_shorten():
    assert shorten("morganna") == "mrgnn"
    assert shorten("Love") == "Lv"
    assert shorten("sea") == "s"
    assert shorten("123") == "123"
    assert shorten("xbox.") == "xbx."
    assert shorten("Amor") == "mr"