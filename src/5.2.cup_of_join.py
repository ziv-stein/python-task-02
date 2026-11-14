"""Joins several lists into one list with a separator between them."""

DEFAULT_SEP = "-"


def cup_of_join(*lists: list, sep=DEFAULT_SEP) -> list | None:
    """
    Joins lists into one list, with sep between every two lists.

    :param lists: Lists to join
    :param sep: Separator to put between the lists
    :return: The joined list, or None if no lists were given
    """
    if not lists:
        return None

    joined = list(lists[0])
    for current_list in lists[1:]:
        joined += [sep, *current_list]
    return joined


def main():
    """Prints a few example calls."""
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())


if __name__ == "__main__":
    main()
    