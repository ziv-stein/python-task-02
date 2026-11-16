"""Measures how long a function takes to run."""

import time

GREETING = "Hi {name}"


def running_2000(func, *args, **kwargs) -> float:
    """Returns the run time of func in seconds."""
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000(GREETING.format, name="Bug"))
