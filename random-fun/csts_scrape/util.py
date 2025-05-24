import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes import Competition
from config import DATA_DIR

logger = logging.getLogger(__name__)


def click_cookie_button(driver: webdriver.Firefox) -> None:
    """Click the cookie button if it appears on the page."""
    try:
        cookie_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Povolit všechny']"))
        )
        cookie_button.click()
        logger.info("Cookie button clicked.")
    except Exception as e:
        logger.info("Cookie button not found or not clickable:", e)


def save_competition_to_json(competition: Competition) -> None:
    """Save competition data to a JSON file."""
    filename = competition.gen_filename()
    with open(f"{DATA_DIR}/{filename}", "w+", encoding="utf-8") as f:
        try:
            json.dump(competition.to_dict(), f, ensure_ascii=False, indent=2)
            logger.info(f"Competition data saved to {filename}.")
        except Exception as e:
            logger.error(f"Error saving competition data to JSON: {e}")
            raise e
