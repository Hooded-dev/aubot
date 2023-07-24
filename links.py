import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def is_admission_link(link):
    keyword_pattern = re.compile(r'Admission|admissions|Faculties', re.IGNORECASE)
    return bool(keyword_pattern.search(link))

def links():
    links_list = urls
    all_links = []
    for link in links_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        base_url = response.url  # Get the base URL from the response object
        links = []
        for a_tag in soup.find_all("a"):
            href = a_tag.get("href")
            if href:
                absolute_link = urljoin(base_url, href)  # Convert relative link to absolute link
                if is_admission_link(absolute_link):
                    links.append(absolute_link)
        all_links.extend(links)
#    print(len(all_links))
    with open('links.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(all_links))
    return all_links

urls = ["https://au.edu.pk/"]
all_links = links()
