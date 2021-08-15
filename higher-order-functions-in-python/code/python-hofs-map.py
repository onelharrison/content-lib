def first_name(full_name: str) -> str:
    """Extracts and returns the first name from a full name"""
    return full_name.split(" ")[0]


def square(n: int) -> int:
    """Returns the square of the given number"""
    return n ** 2


full_names = ["Ada Lovelace", "Katherine Johnson", "Marie Curie"]

first_names = list(map(first_name, full_names))

print(first_names)  # ["Ada", "Katherine", "Marie"]

squares = list(map(square, range(1, 10)))

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
