import logging
import time
import arrow
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from classes import Competition, Category
from config import NAME_TO_MONTH

logger = logging.getLogger(__name__)


def get_competitions(driver: webdriver.Firefox) -> list[Competition]:
    """Get all competition buttons."""
    try:
        competition_buttons = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='txqkl5d']")
            )
        )
        logger.info("Competition buttons found.")
    except Exception as e:
        logger.error("Competition buttons not found:", e)
        raise e

    try:
        # Extract competition data from buttons
        logger.info("Extracting competition data from buttons.")
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

        logger.info("Competition data extracted successfully.")
        return competitions
    except Exception as e:
        logger.error("Error extracting competition data:", e)
        raise e


def get_competition_categories(
    driver: webdriver.Firefox, competition: Competition
) -> list[Category]:
    """Get all competition categories."""
    try:
        # Click the competition button
        competition.button.click()
        logger.info(f"Competition button clicked: {competition.name}")

        time.sleep(1)  # Wait for the categories to load
        category_div = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div._1rsl8qj0._1rsl8qj1._1j7rp576t")
            )
        )
        logger.info("Category div present.")

        # Find all category buttons
        categories = category_div.find_elements(By.XPATH, "//a[@class='_1g61z7h0']")

        # Filter out the first category (which is just link to home page)
        categories = categories[1:]
        logger.info("Competition categories found.")
    except Exception as e:
        logger.error("Competition categories not found:", e)
        raise e

    # Extract category data from buttons
    try:
        logger.info("Extracting category data from buttons.")
        categories_list = []
        for button in categories:
            name = button.text
            category = Category(name=name, link=button.get_attribute("href"))
            categories_list.append(category)

        logger.info("Category data extracted successfully.")

        # Close the category div
        competition.button.click()

        return categories_list
    except Exception as e:
        logger.error("Error extracting category data:", e)
        raise e
