## REMINDER:
# why need join() and split() INSTEAD of strip()
## REASON: --->  4                semesters <---
from src.utils.logging import get_logger

def get_based_criteria(html_content):
    logger = get_logger("Get Based Criteria")

    program_nameObj = html_content.find('h1')
    if program_nameObj:
        program_name = " ".join(program_nameObj.text.split())
    else:
        logger.warning("Could not find the program_name element.")
        program_name = None


    degreeTypeObj = html_content.find('span', attrs={"class":"status abschluss"})
    if degreeTypeObj:
        degreeType = " ".join(degreeTypeObj.text.split())
    else:
        logger.warning("Could not find the degreeType element.")
        degreeType = None


    durationObj = html_content.find('span', attrs={"class":"status regelstudienzeit"})
    if durationObj:
        duration = " ".join(durationObj.text.split())
    else:
        logger.warning("Could not find the duration element.")
        duration = None


    studyModeObj = html_content.find('span', attrs={"class":"status besform"})
    if studyModeObj:
        studyMode = " ".join(studyModeObj.text.split())
    else:
        logger.warning("Could not find the studyMode element.")
        studyMode = None


    locationObj = html_content.find('span', attrs={"class":"status studienstandort"})
    if locationObj:
        location = " ".join(locationObj.text.split())
    else:
        logger.warning("Could not find the location element.")
        location = None


    universityObj = html_content.find('span', attrs={"class":"status name"})
    if universityObj:
        university = " ".join(universityObj.text.split())
    else:
        logger.warning("Could not find the university element.")
        university = None


    programURLObj = html_content.find("a", attrs={"class": "btn btn-light btn-link"})
    if programURLObj:
        programURL = programURLObj['href']
    else:
        logger.warning("Could not find the URL element.")
        programURL = None


    languageObj = html_content.find('span', attrs={"class":"status hauptsprache"})
    if languageObj:
        language = " ".join(languageObj.text.split())
    else:
        logger.warning("Could not find the language element.")
        language = None


    areaOfStudyObj = html_content.find('span', attrs={"class":"tooltip hidden-print"})
    if areaOfStudyObj:
        areaOfStudy = areaOfStudyObj.next_siblings
        subject = ','.join(list(areaOfStudy)).strip()
    else:
        logger.warning("Could not find the areaOfStudy element.")
        subject = None


    return {
            "program_name": program_name,
            "program_url": programURL,
            "university": university,
            "location": location,
            "duration": duration,
            "degreeType": degreeType,
            "language": language,
            "subject": subject,
            "studyMode": studyMode
        }