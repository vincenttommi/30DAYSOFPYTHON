import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs"
page =  requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")


results = soup.find(id="ResultsContainer")


print(results.prettify())

jobs_elements  =  results.find_all("div",class_="card-content")

#iterating those job elements

for  job_element in job_elements:
    print(jobs_elements, end="\n"* 2)
    
    
    
    
    for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()