"""One liner for linting purposes."""


def addition_typed(n1: int, n2: int) -> int:
    """Summary line does this need to be longer.

    Description of content here.
    Args:
        n1 (int): number 1
        n2 (int): number 2

    Returns:
        sum of n1 and n2
    """
    return n1 + n2


# Should work
print(addition_typed(2, 3))

# Mypy issue
print(addition_typed("a", "b"))
