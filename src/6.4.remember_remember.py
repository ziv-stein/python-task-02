from PIL import Image


def remember_remember(path):
    """Returns the secret message hidden in the image."""
    image = Image.open(path)
    width, height = image.size
    message = ""
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) != 255:
                message += chr(y)
    return message


if __name__ == "__main__":
    print(remember_remember("resources/code.png"))