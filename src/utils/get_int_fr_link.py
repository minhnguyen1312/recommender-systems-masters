import re

def utils_get_last_seq_from_str(str):
    """
        This function extracts the last numeric sequence from a string
        Primarily used to return the total number of programs found on url link
    """
    match = re.findall(r'\d+(?:\.\d+)*', str)
    if match:
        return match[-1]
    
def extract_digit_from_url(url):
    """
    Extracts the digit from the given URL.

    Parameters:
    - url (str): The URL containing the digit.

    Returns:
    - int: The extracted digit as an integer, or None if no digit is found.
    """
    match = re.search(r'/pn/(\d+)\.html', url)
    if match:
        return int(match.group(1))  # Convert the extracted digit to an integer
    return None