"""Interleaves several iterables into one list."""


def interleaves(*iterables) -> list:
    """
    Returns a list of the items of the iterables, interleaved.

    :param iterables: Iterables to interleave
    :return: Interleaved list
    """
    return [item for group in zip(*iterables) for item in group]


def main():
    """Prints an example call."""
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))


if __name__ == "__main__":
    main()
