import logging
import arrow
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from config import *
import time


@dataclass
class Competitor:
    name: str
    placement: int
    grades: list[str]

    def __repr__(self) -> str:
        return f"{self.name} {self.placement} {self.grades}"


@dataclass
class Category:
    name: str
    link: str | None
    competitors: list[Competitor] | None = None
    judges: list[str] | None = None

    def __repr__(self) -> str:
        return f"{self.name} {self.link}"


@dataclass
class Competition:
    date: arrow.Arrow
    town: str
    name: str
    button: WebElement
    categories: list[Category] | None = None

    def __repr__(self) -> str:
        return f"{self.date.format('YYYY-MM-DD')} {self.town} {self.name}"


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)


def init_driver() -> webdriver.Firefox:
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver


def click_cookie_button(driver: webdriver.Firefox) -> None:
    """Click the cookie button if it appears on the page."""
    try:
        cookie_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Povolit všechny']"))
        )
        cookie_button.click()
        logging.info("Cookie button clicked.")
    except Exception as e:
        logging.info("Cookie button not found or not clickable:", e)


def select_month(driver: webdriver.Firefox, month: int) -> None:
    # Click on the month button
    try:
        month_button = driver.find_element(By.XPATH, "//button[@aria-label='Měsíc']")
        month_button.click()
        logging.info("Month button clicked.")
    except Exception as e:
        print("Month button not found or not clickable:", e)
        logging.error("Month button not found or not clickable:", e)
        raise e

    # Wait for the month list to be present
    try:
        month_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )
        month_list = month_list.find_element(By.XPATH, ".//div[@role='presentation']")
        logging.info("Month list found.")
    except Exception as e:
        logging.error("Month list not found:", e)
        raise e

    # Find the div containing the month and click it
    try:
        month_div = month_list.find_elements(By.XPATH, f"//div[@role='option']")[
            month - 1
        ]
        month_div.click()
        logging.info(f"Month {month} clicked.")
    except Exception as e:
        logging.error(f"Month {month} not found in the list:", e)
        raise e


def get_competitions(driver: webdriver.Firefox) -> list[Competition]:
    """Get all competition buttons."""
    try:
        competition_buttons = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='txqkl5d']")
            )
        )
        logging.info("Competition buttons found.")
    except Exception as e:
        logging.error("Competition buttons not found:", e)
        raise e

    try:
        # Extract competition data from buttons
        logging.info("Extracting competition data from buttons.")
        competitions = []
        for button in competition_buttons:
            month, day, town, name = tuple(button.text.split("\n"))
            competition = Competition(
                date=arrow.get(f"2025-{NAME_TO_MONTH[month]}-{day}", "YYYY-M-D"),
                town=town,
                name=name,
                button=button,
            )
            competitions.append(competition)

        logging.info("Competition data extracted successfully.")
        return competitions
    except Exception as e:
        logging.error("Error extracting competition data:", e)
        raise e


def get_competition_categories(
    driver: webdriver.Firefox, competition: Competition
) -> list[Category]:
    """Get all competition categories."""
    try:
        # Click the competition button
        competition.button.click()
        logging.info(f"Competition button clicked: {competition.name}")

        time.sleep(1)  # Wait for the categories to load
        category_div = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div._1rsl8qj0._1rsl8qj1._1j7rp576t")
            )
        )
        logging.info("Category div present.")

        # Find all category buttons
        categories = category_div.find_elements(By.XPATH, "//a[@class='_1g61z7h0']")

        # Filter out the first category (which is just link to home page)
        categories = categories[1:]
        logging.info("Competition categories found.")
    except Exception as e:
        logging.error("Competition categories not found:", e)
        raise e

    # Extract category data from buttons
    try:
        logging.info("Extracting category data from buttons.")
        categories_list = []
        for button in categories:
            name = button.text
            category = Category(name=name, link=button.get_attribute("href"))
            categories_list.append(category)

        logging.info("Category data extracted successfully.")

        # Close the category div
        competition.button.click()

        return categories_list
    except Exception as e:
        logging.error("Error extracting category data:", e)
        raise e


# Initialize the WebDriver
driver = init_driver()
driver.get(BASE_URL)

# Wait for the page to load and the cookie button to be clickable
click_cookie_button(driver)

# Select the month
select_month(driver, 1)

# Create a list of competitions
competitions = get_competitions(driver)

# Sort competitions by date
competitions.sort(key=lambda x: x.date)

# Get categories for each competition
for competition in competitions:
    try:
        categories = get_competition_categories(driver, competition)
        competition.categories = categories
        logging.info(f"Categories for {competition.name}: {categories}")
    except Exception as e:
        logging.error(f"Error getting categories for {competition.name}: {e}")


# year_button = driver.find_element(By.XPATH, "//button[@aria-label='Rok']")

driver.quit()
