import pandas as pd

from src.utils.logging import get_logger
import threading
from queue import Queue
from src.web_scraper.threaded_process import process_url

def scrape_multiplethread_program_data():
    logger = get_logger("::::Multi Thread logger::::")
    """
     Main function to create threads and distribute URLs across them.
    """

    output_file="src/data/course_links.csv"
    with open (output_file, 'r') as file:
        df = pd.read_csv(file)
        url_list = df['0'].to_list()


    continue_url = 0

    # Create a thread-safe queue and add URLs to it
    queue = Queue()
    for i in range(continue_url, len(url_list)):
        queue.put(url_list[i])
    # Number of threads to create
    num_threads = 5
    # Create and start threads
    threads = []

    logger.info(f"Initializing {num_threads} threads")
    for i in range(num_threads):
        thread_name = f"Thread-{i+1}"
        thread = threading.Thread(target=process_url, args=(queue, thread_name))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    logger.info("All threads have completed processing URLs.")