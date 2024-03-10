import copy
import os
from bs4 import BeautifulSoup
import unidecode as ud
from html2image import Html2Image


def create_card(
    names: list[str], subjects: list[str], template_file: str, output_name: str
) -> None:
    root_dir = os.path.dirname(os.path.abspath(__file__))

    with open(f"template/{template_file}", "r", encoding="utf-8") as file:
        template = BeautifulSoup(file, "html.parser")

    # Copy cards
    content = template.find("div", {"class": "content"})
    card_container = content.find("div", {"class": "card-container"})
    for _ in range(len(names) - 1):
        content.append(copy.copy(card_container))

    # Fill cards
    cards = content.find_all("div", {"class": "card"})
    for i, card in enumerate(cards):
        image_name = ud.unidecode(names[i]).replace(" ", "_").lower()
        card.find("img")["src"] = os.path.join(root_dir, "imgs", f"{image_name}.png")
        card.find("h2").append(names[i])
        card.find("p").append(subjects[i])

    # Save card as HTML
    with open(f"cards/{output_name}.html", "w", encoding="utf-8") as file:
        file.write(template.prettify())

    # Save card as image
    hti = Html2Image(size=(1200, 825), output_path="cards")
    hti.screenshot(
        html_file=f"cards/{output_name}.html",
        save_as=f"{output_name}.png",
    )
