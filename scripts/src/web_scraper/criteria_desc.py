from src.utils.logging import get_logger

def get_description_criteria(html_content):
  logger = get_logger("Get Admission Criteria")

  overview = html_content.find('div', attrs={"class":"block uebersicht first-block"})
  if overview:
    overview = overview.find("div", attrs={"class":"block-description"}).text.split()
  else:
    logger.warning("Could not find university overview")
    overview = None

  teaching = html_content.find('div', attrs={"class":"block studium"})
  if teaching:
    teaching = teaching.find("div", attrs={"class":"block-description"}).text.split()
  else:
    logger.warning("Could not find university teaching and study description")
    teaching = None

  researching = html_content.find('div', attrs={"class":"block forschung last-block"})
  if researching:
    researching = researching.find("div", attrs={"class":"block-description"}).text.split()
  else:
    logger.warning("Could not find university researching")
    researching = None

  return {
    "overview": overview,
    "teaching": teaching,
    "researching": researching
  }