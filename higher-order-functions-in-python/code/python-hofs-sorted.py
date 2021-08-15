from typing import Any, Tuple

Pair = Tuple[Any, Any]


def pair_first(pair: Pair) -> Any:
    """Returns the first item in a given pair"""
    return pair[0]


def pair_second(pair: Pair) -> Any:
    """Returns the second item in a given pair"""
    return pair[1]


people = [("Marie Curie", 66), ("Katherine Johnson", 101), ("Ada Lovelace", 36)]

# Sort the list by name and print it
print(sorted(people, key=pair_first))

# Sort the list by age and print it
print(sorted(people, key=pair_second))
