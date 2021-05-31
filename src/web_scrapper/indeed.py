import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit=50&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    # make the soup to know how many pages
    # soup is object that allows to look at data of html
    soup = BeautifulSoup(result.text, "html.parser")
    # pagination is another soup that finds what is inside find()
    pagination = soup.find("div", {"class":"pagination"}) # find(name, attributes)

    # find all the links in 'a'
    links = pagination.find_all('a')

    # need to extract the spans in 'a'
    pages = [] 
    for link in links[:-1]:
        pages.append(int(link.string)) # get the string inside the span and append it to list    

    # save the last/max page
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
    return jobs