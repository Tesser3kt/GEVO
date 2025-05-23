import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from config import *
from util import click_cookie_button
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
    handlers=[logging.FileHandler("app.log")],
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def init_driver() -> webdriver.Firefox:
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver


def select_month(driver: webdriver.Firefox, month: int) -> None:
    # Click on the month button
    try:
        month_button = driver.find_element(By.XPATH, "//button[@aria-label='Měsíc']")
        month_button.click()
        logger.info("Month button clicked.")
    except Exception as e:
        print("Month button not found or not clickable:", e)
        logger.error("Month button not found or not clickable:", e)
        raise e

    # Wait for the month list to be present
    try:
        month_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )
        month_list = month_list.find_element(By.XPATH, ".//div[@role='presentation']")
        logger.info("Month list found.")
    except Exception as e:
        logger.error("Month list not found:", e)
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


def select_year(driver: webdriver.Firefox, year: int) -> None:
    # Click on the year button
    try:
        year_button = driver.find_element(By.XPATH, "//button[@aria-label='Rok']")
        year_button.click()
        logger.info("Year button clicked.")
    except Exception as e:
        print("Year button not found or not clickable:", e)
        logger.error("Year button not found or not clickable:", e)
        raise e

    # Wait for the year list to be present
    try:
        year_list = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )
        year_list = year_list.find_element(By.XPATH, ".//div[@role='presentation']")
        logger.info("Year list found.")
    except Exception as e:
        logger.error("Year list not found:", e)
        raise e

    # Find the div containing the year and click it
    try:
        year_div = year_list.find_elements(By.XPATH, f"//div[@role='option']")[year - 1]
        year_div.click()
        logger.info(f"Year {year} clicked.")
    except Exception as e:
        logger.error(f"Year {year} not found in the list:", e)
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


driver.quit()
