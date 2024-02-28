import urllib.request
from unidecode import unidecode


def download_teacher_image(teacher: dict) -> None:
    """Download an image from a URL."""
    name = unidecode(teacher["name"]).replace(" ", "_").lower()
    if (url := teacher["image_url"]) is None:
        return

    urllib.request.urlretrieve(url, f"imgs/{name}.png")
