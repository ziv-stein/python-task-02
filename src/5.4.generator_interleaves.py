"""Interleaves several iterables, one item at a time."""


def generator_interleaves(*iterables):
    """
    Yields the items of the iterables, interleaved.

    :param iterables: Iterables to interleave
    :return: Generator of interleaved items
    """
    for group in zip(*iterables):
        yield from group


def main():
    """Prints an example call."""
    print(list(generator_interleaves("abc", [1, 2, 3], ("!", "@", "#"))))


if __name__ == "__main__":
    main()
