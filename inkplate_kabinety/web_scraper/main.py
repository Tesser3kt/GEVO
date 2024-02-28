import requests
import yaml
from bs4 import BeautifulSoup
import unicodedata


def scrape_web(url: str, timeout: float) -> BeautifulSoup:
    """Scrape the web and return a BeautifulSoup object."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    return BeautifulSoup(response.content, "html.parser")


def load_config(config_path: str) -> dict:
    """Load the configuration from a file."""
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    """Main entry point of the app."""
    config = load_config("config.yaml")

    # Scrape the web
    soup = scrape_web(config.get("url"), config.get("timeout"))

    # Get teachers data
    teachers_data = []
    teachers = soup.find("div", {"id": "kontakty-ucitele-jm"})

    for teacher_block in teachers.find_all("div", {"class": "block"}):
        if (img := teacher_block.find("img")) is None:
            continue
        if (text_block := teacher_block.find("div", {"class": "text-block"})) is None:
            continue
        if (name_and_subject := text_block.contents[0]) is None:
            continue

        name_and_subject = unicodedata.normalize("NFKD", name_and_subject.text)

        if len(name_and_subject.split("\n")) > 2:
            name_and_subject = "\n".join(name_and_subject.split("\n")[:2])

        name, subject = name_and_subject.split("\n")
        img_url = img["data-srcset"].split(" ")[0]

        surname = name.split()[-1]
        name = name.replace(surname, "").strip()
        surname = surname.lower().capitalize()

        name = f"{name} {surname}"

        teachers_data.append({"name": name, "subject": subject, "img_url": img_url})

    # Save the data to CSV
    with open("../teachers.csv", "w", encoding="utf-8") as file:
        file.write("Name,Subject,Image URL\n")
        for teacher in teachers_data:
            file.write(f"{teacher['name']};{teacher['subject']};{teacher['img_url']}\n")


if __name__ == "__main__":
    main()
