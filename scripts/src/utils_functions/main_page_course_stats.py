from bs4 import BeautifulSoup
from utils.get_int_fr_link import utils_get_last_seq_from_str


"""
  Extracting course-related statistics on the main page of the website.
"""

def number_of_courses(filename):
  #  Parse the file content into a BeautifulSoup object 
  with open(filename, "r") as f:
    soup = BeautifulSoup(str(f.read()), 'html.parser')

    # Find & # Extract the text content from the found tag
    view = soup.find('p', attrs={"class":"results-heading"})
    result = view.text
    result = utils_get_last_seq_from_str(result)
    print(result + " programmes found")
    return result
  

def number_of_pages(filename):
  with open(filename, "r") as f:
    soup = BeautifulSoup(str(f.read()), 'html.parser')

    # Find all <li> tags within the <ul>
    li_tags = soup.find('ul', attrs={'class':'pagination'}).find_all('li')
    # get number of page <-- second to last digit of <li> tags
    view = li_tags[-2]
    result = view.text.strip(" \t\n\r")

    print(result + " pages found")
    return result