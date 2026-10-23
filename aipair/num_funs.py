# create following functions
# isprime(n): returns True if n is a prime number, False otherwise
# isperfect(): returns True if n is a perfect number, False otherwise
# ispalindrome(s : int): returns True if s is a palindrome, False otherwise


def isprime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isperfect(n: int) -> bool:
    """Return True if n is a perfect number, False otherwise."""
    if n <= 1:
        return False
    divisors_sum = 1  # 1 is a divisor of every number > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid counting the square root twice for perfect squares
                divisors_sum += n // i
    return divisors_sum == n    


def ispalindrome(s: int) -> bool:
    """Return True if s is a palindrome, False otherwise."""
    s_str = str(s)
    return s_str == s_str[::-1]


