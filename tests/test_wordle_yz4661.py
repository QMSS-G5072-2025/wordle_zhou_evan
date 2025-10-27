from wordle_yz4661.wordle_yz4661 import validate_guess, check_guess

import pytest


# Word list for testing
WORD_LIST = [
    "crane", "apple", "hello", "world", "python", 
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    """
    # Valid guesses
    assert validate_guess("crane") is True
    assert validate_guess("cranee",  6)  is True
    
    # Invalid guesses
    assert validate_guess("cranee", 5) is False
    assert validate_guess("cranE") is False
    assert validate_guess("cran1") is False  
    assert validate_guess("cran~") is False 
    assert validate_guess("cran~1", 6) is False 

    # Edge cases
    assert validate_guess("") is False
    assert validate_guess(None) is False
    assert validate_guess(123) is False

def test_check_guess():
    """
    Test basic check_guess functionality.
    """
    # Perfect match
    secret, guess = "crane", "crane"
    expected = [(c, "green") for c in guess]
    assert check_guess(secret, guess) == expected

    # No match
    secret, guess = "crane", "books"
    expected = [(c, "gray") for c in guess]
    assert check_guess(secret, guess) == expected

    # Mixed results
    secret, guess = "crane", "camps"
    expected = [("c", "green"),("a", "yellow"),
                ("m", "gray"), ("p", "gray"), ("s", "gray") ]
    assert check_guess(secret, guess) == expected

    # Edge cases
    secret, guess = "crane", "hi"
    expected = []
    assert check_guess(secret, guess) == expected