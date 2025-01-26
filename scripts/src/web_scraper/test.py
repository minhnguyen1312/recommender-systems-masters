# import pandas as pd
# def generate_url_list(base_url, start, end):
#     """
#     Generates a list of URLs with the digit placeholder replaced by a range of numbers.

#     Parameters:
#     - base_url (str): The base URL with a placeholder `{digit}`.
#     - start (int): The starting number for the range.
#     - end (int): The ending number for the range (inclusive).

#     Returns:
#     - list: A list of URLs with `{digit}` replaced by numbers from start to end.
#     """
#     return [base_url.format(digit=i) for i in range(start, end + 1)]

# def save_urls_to_csv(urls, file_path):
#     """
#     Saves a list of URLs to a CSV file.

#     Parameters:
#     - urls (list): The list of URLs to save.
#     - file_path (str): The file path for the CSV file.
#     """
#     # Example usage
#     base_url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3/pn/{digit}.html?tx_szhrksearch_pi1%5Babschluss%5D%5B0%5D=37&tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"
#     urls = generate_url_list(base_url, 0, 10500)

#     df = pd.DataFrame(urls, columns=["URL"])
#     df.to_csv("course_links.csv")
#     print(f"Saved {len(urls)} URLs to course_links.csv")
#     # Print the first 5 URLs as a preview
#     print(urls[:5])


# # Example usage
# base_url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3/pn/{digit}.html?tx_szhrksearch_pi1%5Babschluss%5D%5B0%5D=37&tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"
# urls = generate_url_list(base_url, 0, 10500)
# save_urls_to_csv(urls, "urls.csv")
















from src.utils.get_int_fr_link import extract_digit_from_url

url = "https://www.hochschulkompass.de/en/degree-programmes/study-in-germany-search/advanced-degree-programme-search/detail/all/search/1/studtyp/3/pn/105.html?tx_szhrksearch_pi1%5Babschluss%5D%5B0%5D=37&tx_szhrksearch_pi1%5Bresults_at_a_time%5D=100"
digit = extract_digit_from_url(url)
print(f"Extracted digit: {digit}")
