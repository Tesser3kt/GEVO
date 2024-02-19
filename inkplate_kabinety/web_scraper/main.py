import requests
import yaml
from bs4 import BeautifulSoup


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

    soup = scrape_web(config.get("url"), config.get("timeout"))
    print(soup.prettify())


if __name__ == "__main__":
    main()
