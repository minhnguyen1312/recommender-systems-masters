# Use selenium webdriver to remotely scrap data from websites
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from src.utils.logging import get_logger
import time

def init_driver(max_retries=3, delay=5):
    """
    Initializes a headless Firefox WebDriver with retry logic if initialization fails.

    Parameters:
    - max_retries (int): Maximum number of retries to initialize the WebDriver.
    - delay (int): Delay in seconds between retries.

    Returns:
    - driver (webdriver.Firefox): A headless Firefox WebDriver instance.

    Raises:
    - RuntimeError: If the driver fails to initialize after the specified retries.
    """
    logger = get_logger("init_driver")
    attempts = 0

    while attempts < max_retries:
        try:
            # Increment the attempt counter
            logger.info(f"Attempt {attempts} to initialize the Firefox WebDriver.")

            # Set Firefox options for headless mode
            opts = FirefoxOptions()
            opts.add_argument("--headless")
            
            # Initialize the WebDriver
            driver = webdriver.Firefox(options=opts)

            # Log successful initialization and return the driver
            logger.info("The Firefox WebDriver has been initialized successfully.")
            driver.get("https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/search/1/studtyp/3/pn/0.html?tx_szhrksearch_pi1%5Babschluss%5D%5B0%5D=37&tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100")
            return driver
        except Exception as e:
            logger.error(f"Failed to initialize the WebDriver on attempt {attempts}. Error: {e}")
            if attempts < max_retries:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.critical("Exceeded maximum retries. Unable to initialize the WebDriver.")
                raise RuntimeError("Failed to initialize the Firefox WebDriver after multiple attempts.") from e
