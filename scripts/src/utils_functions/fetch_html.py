from bs4 import BeautifulSoup
import time

def fetch_and_save_html(driver, url, pagename):
    """
      This function fetches the HTML content of a webpage, saves it to a file, and returns the file name.
      Args:
        driver: A Selenium WebDriver instance used to interact with the browser.
        url: The URL of the webpage to fetch.
        pagename: The name of the file where the HTML content will be saved.
      Return: name of file
    """
    soup = fetch_page_as_soup(driver, url)

    with open (pagename, 'w') as file:
      file.write(soup.prettify())

    return file.name


def fetch_page_as_soup(driver, url):
    """
      This function fetches the HTML content of a webpage and returns it as a BeautifulSoup object for further processing.
      Args:
        driver: A Selenium WebDriver instance used to interact with the browser.
        url: The URL of the webpage to fetch.
      Return: BeautifulSoup Object of HTML content
    """
    driver.get(url)
    innerHTML = driver.execute_script("return document.body.innerHTML").strip()
    soup = BeautifulSoup(innerHTML, 'html.parser')
    return soup