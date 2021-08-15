from math import floor, sqrt


def is_even(num: int) -> bool:
    """Returns True if a given number is even, otherwise False"""
    return num % 2 == 0


def is_prime(num: int) -> bool:
    """Returns True if a given number is prime, otherwise False"""
    if num <= 1:
        return False

    for factor in range(2, floor(sqrt(num) + 1)):
        if num % factor == 0:
            return False

    return True


nums = range(1, 10)


evens = list(filter(is_even, nums))
primes = list(filter(is_prime, nums))

print(evens)  # [2, 4, 6, 8]
print(primes)  # [2, 3, 5, 7]
