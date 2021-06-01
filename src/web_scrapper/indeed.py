import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

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

def extract_job(html):
    h2_items = html.find_all("h2", {"class": "jobTitle"})
    for h2_item in h2_items:
        all_spans = h2_item.find_all("span")
        for all_span in all_spans:
        # # soup.find("div").get('class') # 속성 값이 없다면 None 반환
            if all_span.get("title") is not None:
                job_name = all_span.get("title")
    companys = html.find_all("span", {"class": "companyName"})
    for company in companys:
        if company.find("a") is not None:
            company_name = company.find("a").string
        else:
            company_name = company.string
    locations = html.find_all("div", {"class": "companyLocation"})
    for location in locations:
        if location.string is not None:
            location_name = location.string
        else:
            location_name = "Remote"
    return {'job': job_name, 'company': company.name, 'location': location_name}

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("td", {"class": "resultContent"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs
