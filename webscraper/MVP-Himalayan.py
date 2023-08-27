from selenium import webdriver
from bs4 import BeautifulSoup
import re


def list_gather(search_query, n_pages=5):  # default to 5 pages, but you can change whenever
    driver = webdriver.Chrome()
    google_url = "https://www.google.com"
    driver.get(google_url)

    query = search_query
    links = []

    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + \
            query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))

    driver.quit()
    return links


# Query for himalayan store
search_query = "Himalayan store"
links = list_gather(search_query)

for link in links:
    print(link)


def second():
    driver = webdriver.Chrome()
    for link in links:
        target_url = link

        driver.get(target_url)

        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
        html = driver.page_source
        emails = re.findall(email_pattern, html)

        print(emails)


second()
