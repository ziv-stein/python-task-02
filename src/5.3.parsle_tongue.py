"""Extracts secret messages hidden inside a binary file."""

import string

LOGO_PATH = "resources/logo.jpg"
CHUNK_SIZE = 1024
MIN_MESSAGE_LENGTH = 5
MESSAGE_END = "!"


def read_chars(file_path: str):
    """
    Reads a binary file in chunks and yields it one character at a time.

    :param file_path: Path to the file
    :return: Generator of single characters
    """
    with open(file_path, "rb") as file:
        while chunk := file.read(CHUNK_SIZE):
            for byte in chunk:
                yield chr(byte)


def parsle_tongue(file_path: str):
    """
    Yields the secret messages hidden in a binary file.

    :param file_path: Path to the file
    :return: Generator of secret messages
    """
    letters = ""
    for char in read_chars(file_path):
        if char in string.ascii_lowercase:
            letters += char
            continue
        if char == MESSAGE_END and len(letters) >= MIN_MESSAGE_LENGTH:
            yield letters + MESSAGE_END
        letters = ""


def main():
    """Prints all secret messages in the course logo."""
    try:
        for message in parsle_tongue(LOGO_PATH):
            print(message)
    except FileNotFoundError:
        print(f"Error: file '{LOGO_PATH}' not found")


if __name__ == "__main__":
    main()