from dataclasses import dataclass
from lorem import get_paragraph, get_sentence, get_word
from datetime import datetime


@dataclass
class Navigation:
    links = {
        "Já chci Domů": "/",
        "Tento": "/lorem",
        "Muzikal": "/ipsum",
        "Je": "/dolor",
        "Fakt": "/sit",
        "Neco": "/amet",
    }


@dataclass
class Title:
    title = "J. A. R."
    date = "69. 42. 2026"
    subtitle = "Křišťálový prášek, světlo rozjasněné, cesta zmizí."


@dataclass
class About:
    text = get_paragraph(count=5)
    heading = "O muzikálu"


@dataclass
class Footer:
    copyright = "AdÁmkŨv tÍm"


@dataclass
class NewsContainer:
    news_heading = "Novinky"


@dataclass
class News:
    title: str
    date: datetime
    text: str
    author: str

@dataclass
class NewsList:
    news = [
        News(
            title=get_word(count=2),
            date=datetime.fromisoformat("2021-01-01"),
            text="Sed do eiusmod já chci spát tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            author="Nekdo Nejaky",
        ),
        News(
            title=get_word(count=1),
            date=datetime.fromisoformat("1912-04-12"),
            text="troll",
            author="Adamuv Otrok",
        ),
        News(
            title=get_word(count=3),
            date=datetime.fromisoformat("2026-12-24"),
            text=get_sentence(count=3),
            author="Lenka Klepacova",
        ),
        News(
            title=get_word(count=3),
            date=datetime.fromisoformat("2023-12-20"),
            text=get_sentence(count=3),
            author="Admin",
        ),
    ]
