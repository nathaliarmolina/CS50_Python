import pytest
from seasons import validate_birth

def test_validate_birth():
    validate_birth("1985-12-16") == True
    validate_birth("batata") == False
    validate_birth("123456789") == False
    validate_birth("1955-12-28") == True
