from PIL import Image  # pylint: disable=import-error

IMAGE_PATH = "resources/code.png"
WHITE = 255


def remember_remember(path):
    """Returns the secret message hidden in the image."""
    image = Image.open(path)
    width, height = image.size
    message = ""
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) != WHITE:
                message += chr(y)
    return message


if __name__ == "__main__":
    try:
        print(remember_remember(IMAGE_PATH))
    except FileNotFoundError:
        print(f"Error: file '{IMAGE_PATH}' not found")
