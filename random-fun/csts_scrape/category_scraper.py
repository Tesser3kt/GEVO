import logging
import re
from collections import defaultdict
from classes import Category, Competitor, Club, Evaluation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from util import click_cookie_button
from config import APPROVAL_SYMBOLS, DISAPPROVAL_SYMBOLS

logger = logging.getLogger(__name__)


def get_jurors(driver: webdriver.Firefox) -> list[str]:
    """Get jurors for a category."""
    try:
        jurors_title = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Porota']"))
        )
        jurors_div = jurors_title.find_element(
            By.XPATH,
            "following-sibling::div[1]",
        )
        logger.info("jurors div present.")

        # Find all jurors (removing (country) by regex)
        jurors_text = jurors_div.text
        parts = re.split(r"\s*\([^)]*\)\s*", jurors_text)
        jurors = list(filter(None, parts))

        return jurors
    except Exception as e:
        logger.error("Error extracting jurors data:", e)
        raise e


def get_category_competitors(
    driver: webdriver.Firefox, category: Category
) -> list[Competitor]:
    """Get competitors for a category."""

    # Wait for at least one of the competitors div to be present.
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='_1rsl8qj0 _1rsl8qj1 _1j7rp5778 x4ja6a8 _1j7rp572g']",
            )
        )
    )

    # Find the competitors div.
    competitor_divs = driver.find_elements(
        By.XPATH,
        "//div[@class='_1rsl8qj0 _1rsl8qj1 _1j7rp5778 x4ja6a8 _1j7rp572g']",
    )

    # Parse the competitors
    competitors = []
    for div in competitor_divs:
        try:
            # Extract competitor data
            competitor_text = div.text
            parts = competitor_text.split("\n")
            if "–" in parts[0]:
                parts[0] = parts[0].split("–")[0]
            placement = int("".join(filter(str.isdigit, parts[0])))
            pair_number = int(parts[1])
            names = tuple(name.strip() for name in parts[2].split("&"))
            for name in names:
                name = " ".join(x.lower().capitalize() for x in name.split())
            club = Club(name=parts[3].strip())

            competitors.extend(
                [
                    Competitor(
                        pair_number=pair_number,
                        name=name,
                        placement=placement,
                        club=club,
                    )
                    for name in names
                ]
            )
        except Exception as e:
            logger.error("Error extracting competitor data:", e)
            continue

    return competitors


def update_category_evaluations(
    driver: webdriver.Firefox, category: Category, round: str
) -> None:
    """Get evaluations for a category."""

    # Navigate to the category link
    if category.link not in driver.current_url:
        # If the current URL is not the category link, navigate to it
        # and click the cookie button.
        logger.info(
            f"Navigating to {category.link}. Different from {driver.current_url}."
        )
        driver.get(category.link)
        click_cookie_button(driver)

    # Wait for the round navigation to be present.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='_1rsl8qj0 _1rsl8qj1 x4ja6ac _1j7rp572x _1j7rp572g x4ja6a8 _1j7rp576t']")  # type: ignore
        )
    )
    try:
        round_button = driver.find_element(By.XPATH, f"//div[text()='{round}']")  # type: ignore
        round_button.click()
        logger.info(f"Round {round} button clicked.")
    except Exception as e:
        logger.info(f"Round {round} button not found or not clickable:", e)
        return

    # Get jury for the current round
    try:
        jurors = get_jurors(driver)
    except Exception as e:
        logger.error("Error getting jurors:", e)
        return

    # Wait for the evaluations div to be present.
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='_1rsl8qj0 _1rsl8qj1 _1j7rp5778 x4ja6a8 _1j7rp572g _1rsl8qj3 _1j7rp576t x4ja6ag']",
            )
        )
    )

    # Get dances div
    dances_div = driver.find_element(
        By.XPATH,
        "//div[@class='_1rsl8qj0 _1rsl8qj1 x4ja6a8 _1j7rp5778 x4ja6a7 _1rsl8qj3 _1j7rp576t x4ja6ag']",
    )
    dances = dances_div.text.split("\n")[:-1]

    evaluation_divs = driver.find_elements(
        By.XPATH,
        "//div[@class='_1rsl8qj0 _1rsl8qj1 _1j7rp5778 x4ja6a8 _1j7rp572g _1rsl8qj3 _1j7rp576t x4ja6ag']",
    )
    for div in evaluation_divs:
        try:
            # Extract evalutation data
            evaluation_text = div.text
            parts = evaluation_text.split("\n")

            pair_number = int(parts[1])

            parts = parts[4:]
            if round != "Finále":
                # Remove all symbols that are not approval symbols or digits
                parts = [
                    part
                    for part in parts
                    if part.isdigit()
                    or part in APPROVAL_SYMBOLS
                    or part in DISAPPROVAL_SYMBOLS
                ]

            for i in range(len(dances)):
                # Read the grades and total grade for each dance
                dance_grades = []

                # The finale round has a different evaluation format
                grade_offset = 0
                placement_offset = 0

                if round == "Finále":
                    grade_offset = i
                    placement_offset = i + len(jurors)

                for j in range(len(jurors)):
                    try:
                        grade_text = parts[i * len(jurors) + j + grade_offset]
                        grade = int(grade_text)
                    except ValueError:
                        if grade_text in ("−", "N"):
                            grade = 0
                        elif grade_text in ("x", "×", "A", "Y"):
                            grade = 1
                        else:
                            logger.error("Invalid grade format:", grade_text)
                            grade = None
                            continue
                    except IndexError:
                        logger.error("Index out of range for grades:", grade_text)
                        grade = None
                        continue
                    dance_grades.append(grade)

                # The final placement is only available in the finale round
                dance_placement = None
                if round == "Finále":
                    # Add the final placement for the finale round
                    try:
                        dance_placement = float(
                            parts[i * len(jurors) + placement_offset]
                        )
                        dance_grades.append(dance_placement)
                    except ValueError:
                        logger.error("Invalid dance placement format:", parts[i])
                        continue
                    except IndexError:
                        logger.error(
                            "Index out of range for dance placement:", parts[i]
                        )
                        continue

                # Form the evaluation object
                evaluation = Evaluation(
                    round=round,
                    dance=dances[i],
                    grades=dance_grades,
                    jurors=jurors,
                    dance_placement=dance_placement,
                )

                # Find the competitor by pair number
                competitors = [
                    c for c in category.competitors if c.pair_number == pair_number
                ]
                for competitor in competitors:
                    # Add the evaluation to the competitor
                    if competitor.grades is None:
                        competitor.grades = []
                    competitor.grades.append(evaluation)
        except Exception as e:
            logger.error("Error extracting evaluation data:", e)
            continue
