from functools import reduce

from safe_get import safe_get


def dig(collection, *keys, default=None):
    """Get values from a potentially nested collection without raising errors"""

    return reduce(lambda x, y: safe_get(x, y, default), keys, collection)
