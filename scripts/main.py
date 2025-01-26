from src.utils.logging import get_logger
from src.web_scraper.scrape_program_data import scrape_multiplethread_program_data

if __name__ == "main":
    logger = get_logger("main")
    logger.info("Main is running...")

    scrape_multiplethread_program_data()

    logger.info("Finish scraping data...")