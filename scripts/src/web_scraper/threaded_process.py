from src.utils.driver import init_driver
from src.utils.logging import get_logger
from src.web_scraper.criteria_based import get_based_criteria
from src.web_scraper.criteria_admission import get_admission_criteria
from src.web_scraper.criteria_desc import get_description_criteria
from src.utils_functions.fetch_html import fetch_page_as_soup
from src.utils.get_int_fr_link import extract_digit_from_url
import os
import pandas as pd

def process_url(queue, thread_name,file_path = "progammes_df.csv"):
    logger = get_logger(f"{thread_name} ----------> ")
    logger.info(f"Initialize::  Driver of {thread_name}")
    """

    Processes URLs from the queue using a WebDriver. Scrapes detailed data from an individual program page.

    Parameters:
    - queue (Queue): A thread-safe queue containing the URLs to process.
    - thread_name (str): The name of the thread processing the URLs.
    """
    driver = init_driver()
    try:
        while not queue.empty():
            url = queue.get()

            try:
                logger.info(f"{thread_name}: Processing URL: {url}")
                driver.get(url)

                url_index = extract_digit_from_url(url)

                html_content = fetch_page_as_soup(driver, url)
                based_criteria = get_based_criteria(html_content)
                admission_criteria = get_admission_criteria(html_content)
                desc_criteria = get_description_criteria(html_content)
                tmp_dictionary = {"index": url_index,**based_criteria, **admission_criteria, **desc_criteria}
                
                program_df = pd.DataFrame([tmp_dictionary], )
                # programmes_df = pd.concat([programmes_df, pd.DataFrame([tmp_dictionary])], ignore_index=True)

                if not os.path.exists(file_path):
                    # Write with header if file doesn't exist
                    program_df.to_csv(file_path, mode='w', header=True, index=False)
                else:
                    # Append without header if file exists
                    program_df.to_csv(file_path, mode='a', header=False, index=False)


            except Exception as e:
                logger.info(f"{thread_name}: Error processing URL {url}: {e}")
            finally:
                queue.task_done()
    finally:
        driver.quit()
        logger.info(f"{thread_name}: Driver closed.")