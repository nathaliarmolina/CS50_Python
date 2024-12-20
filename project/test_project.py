import pytest
from project import say_name
from project import choose_category
from project import set_category
from project import sort_word
from unittest.mock import patch
import random


def test_set_category():
    assert set_category(4) == ["SPAIN", "MEXICO", "JAMAICA", "BRAZIL", "INDIA", "ARGENTINA", "EGYPT", "PORTUGAL", "MOROCCO", "FRANCE"]
    assert set_category(3) == ["ZEBRA", "COUGAR", "ELEPHANT", "PARROT", "SNAKE", "MONKEY", "GIRAFFE", "HAMSTER", "CHAMELEON", "BUMBLEBEE"]


def test_sort_word():
    category = random.randint(1, 5)
    words = set_category(category)
    magic_word = sort_word(words)
    assert magic_word in words
    pytest.main()


def test_say_name():
    with patch('builtins.input', return_value="Bob"):
        name = say_name()
        assert name == "Bob"
