"""Groups items by the result of a function."""


def group_by(func, iterable):
    """Groups the items of an iterable by the result of func."""
    groups = {}
    for item in iterable:
        key = func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
