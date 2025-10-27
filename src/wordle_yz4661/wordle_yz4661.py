def validate_guess(guess, word_length=5):
    """
    Validates if a guess is valid for Wordle.

    Parameters
    ----------
    guess : str
        The word guess to validate.
    word_length : int, optional
        Expected length of the word (default 5).

    Returns
    -------
    bool
        True if guess is valid, False otherwise.
    
    Examples
    --------
    >>> validate_guess("crane")
    True
    >>> validate_guess("Crane")   # must be lowercase
    False
    >>> validate_guess("abc")     # wrong length
    False
    >>> validate_guess("cr4ne")   # non-letters
    False
    """
    if not isinstance(guess, str):
        return False
    if len(guess) != word_length:
        return False
    if not guess.isalpha():
        return False
    return guess.islower()


def check_guess(secret_word, guess):
    """
    Checks a guess against the secret word and returns color hints.

    Parameters
    ----------
    secret_word : str
        The secret word to guess.
    guess : str
        The player's guess.

    Returns
    -------
    list
        List of tuples (letter, color) where color is 'green', 'yellow', or 'gray'.
    
    Examples
    --------
    >>> check_guess("crane", "cared")
    [('c', 'green'), ('a', 'yellow'), ('r', 'yellow'), ('e', 'yellow'), ('d', 'gray')]

    >>> check_guess("crane", "longer")
    []
    """
    if len(secret_word) != len(guess):
        return []

    result = []
    secret_list = list(secret_word)
    guess_list = list(guess)

    # First pass: mark exact matches (green)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result.append((guess_list[i], 'green'))
            secret_list[i] = None  # Mark as used
            guess_list[i] = None   # Mark as used
        else:
            result.append((guess_list[i], None))  # Placeholder

    # Second pass: mark partial matches (yellow)
    for i in range(len(guess_list)):
        if guess_list[i] is not None:  # Not already marked green
            if guess_list[i] in secret_list:
                result[i] = (guess_list[i], 'yellow')
                # Remove first occurrence from secret_list
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (guess_list[i], 'gray')

    return result


def is_valid_word(word, word_list):
    """
    Checks if a word exists in the valid word list.

    Parameters
    ----------
    word : str
        The word to check.
    word_list : list
        List of valid words.

    Returns
    -------
    bool
        True if word is in the list, False otherwise.
    """
    return word.lower() in [w.lower() for w in word_list]


def calculate_game_score(guesses_used, max_guesses=6):
    """
    Calculates the score for a completed Wordle game.

    Parameters
    ----------
    guesses_used : int
        Number of guesses used to solve the puzzle.
    max_guesses : int, optional
        Maximum allowed guesses (default 6).

    Returns
    -------
    int
        Score from 0 to max_guesses (higher is better).

    Examples
    --------
    >>> calculate_game_score(3)
    4
    >>> calculate_game_score(6)
    1
    >>> calculate_game_score(0)   # invalid (non-positive)
    0
    >>> calculate_game_score(7)   # invalid (exceeds max_guesses)
    0
    """
    if guesses_used <= 0 or guesses_used > max_guesses:
        return 0
    return max_guesses - guesses_used + 1