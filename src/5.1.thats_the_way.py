"""Find files in a folder whose names start with 'deep'."""

import os

DEEP_PREFIX = "deep"
IMAGES_FOLDER = "images"


def thats_the_way(folder_path: str) -> list[str]:
    """Return the names of files in folder_path that start with 'deep'."""
    return [
        file_name
        for file_name in os.listdir(folder_path)
        if file_name.startswith(DEEP_PREFIX)
        and os.path.isfile(os.path.join(folder_path, file_name))
    ]


def main():
    """Print the 'deep' files found in the images folder."""
    try:
        deep_files = thats_the_way(IMAGES_FOLDER)
    except FileNotFoundError:
        print(f"Error: folder '{IMAGES_FOLDER}' not found")
        return
    print(f"Found {len(deep_files)} files: {deep_files}")


if __name__ == "__main__":
    main()
