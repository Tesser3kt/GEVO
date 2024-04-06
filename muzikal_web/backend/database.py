from dataclasses import dataclass
from lorem import get_paragraph, get_sentence, get_word
from datetime import datetime
from typing import Optional


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
    subtitle = "50 4F 4D 4F 43 20 44 52 5A 49 20 4D 45 20 54 55 20 4E 41 53 49 4C 49 4D"


@dataclass
class About:
    text = get_paragraph(count=5)
    heading = "O muzikálu"
    image = "https://www.mahannahsscifiuniverse.com/cdn/shop/articles/will-the-uss-enterprise-ncc-1701-e-still-be-in-service-in-picard-187227_1200x1200.jpg"


@dataclass
class Footer:
    copyright = "AdÁmkŨv tÍm"


@dataclass
class NewsContainer:
    news_heading = "Novinky"


@dataclass
class News:
    id: int
    title: str
    date: datetime
    text: str
    author: str
    image: Optional[str] = None


@dataclass
class NewsList:
    news = [
        News(
            id=0,
            title=get_word(count=2),
            date=datetime.fromisoformat("2021-01-01"),
            text="Sed do eiusmod já chci spát tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            author="Nekdo Nejaky",
            image="https://www.fandimefilmu.cz/files/images/2023/05/10/article_main_qx855vcaa0ql8661.jpg",
        ),
        News(
            id=1,
            title=get_word(count=1),
            date=datetime.fromisoformat("1912-04-12"),
            text="troll",
            author="Adamuv Otrok",
            image="https://www.gevo.cz/files/responsive/640/0/adamklepac.jpg",
        ),
        News(
            id=2,
            title=get_word(count=3),
            date=datetime.fromisoformat("2026-12-24"),
            text=get_sentence(count=100),
            author="Lenka Klepacova",
            image="https://www.gevo.cz/files/responsive/640/0/adamklepac.jpg",
        ),
        News(
            id=3,
            title=get_word(count=3),
            date=datetime.fromisoformat("2023-12-20"),
            text=(
                "Penatibus et magnis dis parturient montes nascetur ridiculus mus mauris. Nibh venenatis cras sed felis eget velit aliquet. Gravida dictum fusce ut placerat. Tristique senectus et netus et malesuada fames ac. Proin libero nunc consequat interdum varius sit amet mattis. Proin sed libero enim sed faucibus turpis in eu. Et ligula ullamcorper malesuada proin libero nunc consequat. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Ante in nibh mauris cursus mattis molestie a iaculis. Donec pretium vulputate sapien nec."
                "Vitae proin sagittis nisl rhoncus mattis rhoncus urna neque. Vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Morbi tristique senectus et netus et. Mi sit amet mauris commodo quis. Tincidunt dui ut ornare lectus. Rhoncus urna neque viverra justo nec ultrices dui sapien. Tortor consequat id porta nibh venenatis cras sed felis eget. Accumsan tortor posuere ac ut consequat semper viverra. Facilisis mauris sit amet massa vitae tortor condimentum lacinia. At auctor urna nunc id."
            ),
            author="Admin",
            image="",
        ),
    ]


@dataclass
class image:
    img: str
    alt: str
    credit: Optional[str] = None


@dataclass
class ImageList:
    imgs = [
        image(
            img="https://upload.wikimedia.org/wikipedia/en/a/aa/X-303_Prometheus_from_the_television_series_Stargate_SG-1.png",
            alt="Adam Klepáč",
        ),
        image(
            img="https://as1.ftcdn.net/v2/jpg/03/16/01/42/1000_F_316014283_yGC7pqaC6QgpH3h08Y1U1M7SH36f3Imr.jpg",
            alt="Adam Klepáč",
        ),
        image(
            img="https://web.dev/images/authors/katiehempenius.jpg",
            alt="Adam Klepáč",
        ),
        image(
            img="https://static.albert.cz/medias/sys_master/h5b/h42/9004464832542.jpg",
            alt="Adam Klepáč",
        ),
    ]
