from utils_functions.main_page_course_stats import number_of_pages
from utils_functions.extract_links import extract_course_links
from utils.driver import init_driver
from utils.logging import get_logger
import pandas as pd 
import re





def get_parent_url():
  logger = get_logger("get_parent_url")
  logger.info("--------------------------------------------")
  logger.info("PART - 1 - Enter URL of main page of course|")
  logger.info("--------------------------------------------")
  
  urlpage = input('Enter Parent URL :')
  return urlpage

def save_couselinks():
  logger = get_logger("save_course_links")
  urlpage = get_parent_url()
  numpages=number_of_pages("mainpage.txt"), 
  output_file="src/data/courselinks.csv"

  links = course_links_scraper(urlpage, numpages)

  with open (output_file, 'w') as file:
    df = pd.DataFrame(links)
    df.to_csv(file)



def course_links_scraper(
    urlpage,
    numpages):
  """
  Scrapes course links from multiple pages of parent url and saves them to a CSV file.

    Parameters:
    - parent_url (str): The base URL of the website where the scraping begins.
    - numpages (int): The total number of pages to scrape.
    - output_file (str): The file path to save the scraped links in CSV format.

    Functionality:
    1. Iterates through the specified number of pages of the website.
    2. Extracts course links from each page using the `extract_course_links` function.
    3. Appends all links to a list.
    4. Saves the collected links to the specified CSV file.

    Output:
    - An list of all the extracted course links.
  """

  links = []
  # Get all pages link from the website
  i = 0
  while i < numpages:
    print(f"======== Going to page {i + 1}")
    links_in_page = extract_course_links(urlpage)
    for eachLink in links_in_page:

      #loginate link and append to list
      eachLink = 'https://www.hochschulkompass.de' + eachLink
      links.append(eachLink)
    urlpage = re.sub(r'/pn/(\d+)', str(i), urlpage)
    i = i + 1

  print(f"There are currently {len(links)} available")

  return links