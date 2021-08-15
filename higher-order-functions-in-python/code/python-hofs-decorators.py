def log_before(f):
    def _wrapper(*args, **kwargs):
        print("logging before...")
        f(*args, **kwargs)

    return _wrapper


def log_after(f):
    def _wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print("logging after...")

    return _wrapper


@log_before
@log_after
def greet(name: str):
    print(f"Hello {name}")


# with the log_before and log_after decorators
# the following is semantically equivalent to
# `log_before(log_after(greet))("John")`
greet("John")
