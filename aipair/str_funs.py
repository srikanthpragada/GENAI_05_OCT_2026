def hasupper(s: str) -> bool:
    """Return True if s has at least one uppercase letter, False otherwise."""
    for char in s:
        if char.isupper():
            return True
    return False


def countupper(s: str) -> int:
    """Return the number of uppercase letters in s."""
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count


