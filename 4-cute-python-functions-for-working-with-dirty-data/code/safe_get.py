def safe_get(collection, key, default=None):
    """Get values from a collection without raising errors"""

    try:
        return collection.get(key, default)
    except TypeError:
        pass

    try:
        return collection[key]
    except (IndexError, TypeError):
        pass

    return default
