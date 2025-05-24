import arrow
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from unidecode import unidecode as ud


@dataclass
class Club:
    name: str

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


@dataclass
class Evaluation:
    round: str
    dance: str
    grades: list[int]
    jurors: list[str]
    dance_placement: float | None = None

    def __repr__(self) -> str:
        return (
            f"{self.dance} ({self.round}): {self.grades} -> {self.dance_placement}"
            if self.round == "Finále"
            else f"{self.dance} ({self.round}): {self.grades}"
        )

    def to_dict(self) -> dict:
        return {
            "round": self.round,
            "dance": self.dance,
            "grades": self.grades,
            "jurors": self.jurors,
            "dance_placement": self.dance_placement,
        }


@dataclass
class Competitor:
    pair_number: int
    name: str
    placement: int
    club: Club | None = None
    grades: list[Evaluation] | None = None

    def __repr__(self) -> str:
        return f"{self.placement}. {self.name} ({self.pair_number}), {self.club}"

    def to_dict(self) -> dict:
        return {
            "pair_number": self.pair_number,
            "name": self.name,
            "placement": self.placement,
            "club": str(self.club),
            "grades": (
                [grade.to_dict() for grade in self.grades] if self.grades else None
            ),
        }


@dataclass
class Category:
    name: str
    link: str | None = None
    competitors: list[Competitor] | None = None

    def __repr__(self) -> str:
        return f"{self.name} {self.link}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "link": self.link,
            "competitors": (
                [competitor.to_dict() for competitor in self.competitors]
                if self.competitors
                else None
            ),
        }


@dataclass
class Competition:
    date: arrow.Arrow
    town: str
    name: str
    button: WebElement
    categories: list[Category] | None = None

    def __repr__(self) -> str:
        return f"{self.date.format('YYYY-MM-DD')} {self.town} {self.name}"

    def to_dict(self) -> dict:
        return {
            "date": self.date.format("YYYY-MM-DD"),
            "town": self.town,
            "name": self.name,
            "categories": (
                [category.to_dict() for category in self.categories]
                if self.categories
                else None
            ),
        }

    def gen_filename(self) -> str:
        """Generate a filename for the competition based on its date, town, and name."""
        date_str = self.date.format("YYYY-MM-DD")
        town_str = (
            ud(
                "".join(
                    x for x in self.town if x.isalpha() or x.isdigit() or x.isspace()
                )
            )
            .replace(" ", "_")
            .lower()
        )
        name_str = (
            ud(
                "".join(
                    x for x in self.name if x.isalpha() or x.isdigit() or x.isspace()
                )
            )
            .replace(" ", "_")
            .lower()
        )
        return f"{date_str}_{town_str}_{name_str}.json"
