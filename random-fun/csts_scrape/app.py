import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from config import *
from util import click_cookie_button, save_competition_to_json
from classes import Competition, Category, Competitor, Evaluation
from competition_scraper import get_competitions, get_competition_categories
from category_scraper import (
    get_category_competitors,
    update_category_evaluations,
)


# Set up logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def init_driver() -> webdriver.Firefox:
    options = Options()
    options.set_preference("dom.webdriver.enabled", False)  # Disable webdriver flag
    options.set_preference(
        "useAutomationExtension", False
    )  # Disable automation extension
    if HEADLESS:
        options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver


def select_month(driver: webdriver.Firefox, month: str) -> None:
    # Click on the month button
    try:
        month_button = driver.find_element(By.XPATH, "//button[@aria-label='Měsíc']")
        month_button.click()
        logger.info("Month button clicked.")
    except Exception as e:
        print("Month button not found or not clickable:", e)
        logger.error("Month button not found or not clickable:", e)
        raise e

    # Wait for the month button to be present
    try:
        month_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )
        month_button = month_list.find_element(By.XPATH, f".//*[text()='{month}']")
        month_button.click()
        logger.info("Month button clicked.")
    except Exception as e:
        logger.error("Month button not found:", e)
        raise e


def select_year(driver: webdriver.Firefox, year: str) -> None:
    # Click on the year button
    try:
        year_button = driver.find_element(By.XPATH, "//button[@aria-label='Rok']")
        year_button.click()
        logger.info("Year button clicked.")
    except Exception as e:
        print("Year button not found or not clickable:", e)
        logger.error("Year button not found or not clickable:", e)
        raise e

    # Wait for the year button to be present
    try:
        year_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )
        year_button = year_list.find_element(By.XPATH, f".//*[text()='{year}']")
        year_button.click()
        logger.info("Year button clicked.")
    except Exception as e:
        logger.error("Year button not found:", e)
        raise e


# Initialize the WebDriver
driver = init_driver()
driver.get(BASE_URL)

# Wait for the page to load and the cookie button to be clickable
click_cookie_button(driver)

# Select the year
select_year(driver, YEAR)

# Select the month
select_month(driver, MONTH)

# Create a list of competitions
competitions = get_competitions(driver)

# Sort competitions by date
competitions.sort(key=lambda x: x.date)

# Get categories for each competition
for competition in competitions:
    try:
        categories = get_competition_categories(driver, competition)
        competition.categories = categories
        logger.info(f"Categories for {competition.name}: {categories}")
    except Exception as e:
        logger.error(f"Error getting categories for {competition.name}: {e}")

# Scrape each category for competitors and evaluations
category = Category(
    name="Test Category",
    link="https://www.csts.cz/dancesport/vysledky_soutezi/event/1293/competition/28733",
)
for competition in competitions:
    for category in competition.categories:
        try:
            driver.get(category.link)
            category_competitors = get_category_competitors(driver, category)
            logger.info(f"Competitors for {category.name}: {category_competitors}")
            category.competitors = category_competitors
            # Update evaluations for each round
            for round in ROUNDS:
                update_category_evaluations(driver, category, round=round)
        except Exception as e:
            logger.error(f"Error getting competitors for {category.name}: {e}")
    # Save competition data to JSON
    save_competition_to_json(competition)


driver.quit()
