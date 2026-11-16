"""Maps each word in a text to its length."""

TEXT = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""


def long_cat_is_long(text: str) -> dict:
    """
    Returns a dictionary of every word in the text and its length.

    :param text: Text to count
    :return: Dictionary of word to length
    """
    clean_text = "".join(char for char in text.lower() if char.isalpha() or char.isspace())
    return {word: len(word) for word in clean_text.split()}


def main():
    """Prints the word lengths of the example text."""
    print(long_cat_is_long(TEXT))


if __name__ == "__main__":
    main()