from utils.driver import driver
from utils_functions.fetch_html import course_page_html




def extract_course_links(url):
  """
    Extracts all course links from the specified URL.

    Args:
        url (str): The URL of the webpage to extract course links from.

    Returns:
        list: A list of strings, each containing a URL to a course.

    Raises:
        requests.exceptions.RequestException: If there's an error fetching the page content.
        ValueError: If the page does not contain any course links.
  """
  links_in_page = []

  #parse the HTML content of URL
  content = course_page_html(driver, url)

  # Find all course links and append to list
  view = content.find_all('a', attrs={'class':'btn-info btn'})
  for i in view:
    links_in_page.append(str(i.attrs['href']))
  
  if not links_in_page:
    raise ValueError("No course links found on the page.")
  
  return links_in_page
    

