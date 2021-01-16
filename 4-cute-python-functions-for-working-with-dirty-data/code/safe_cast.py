def safe_cast(value, astype, default=None):
    """Convert one type to another without raising errors"""

    try:
        return astype(value)
    except (TypeError, ValueError):
        pass

    return default
