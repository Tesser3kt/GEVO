import json
import unidecode
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes import Competition

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
    """Convert a Competition object to a JSON-compatible dictionary."""
