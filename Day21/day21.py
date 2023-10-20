import requests
from  bs4 import   BeautifulSoup


"""sumary_line
1. Write a Python program that uses web scraping to extract the title and price of a product from an online shopping website. Print the extracted informatio
"""

url  =  'https://www.example.com/product-page'


#sending an Http request to URL
response  =  requests.get(url)

#checking if request was  successful
if  response.status_code == 200:
    #Parse the HTML content of the page using BeautifulSoup
    soup =  BeautifulSoup(response.text, 'html.parser')
    
    
    
    #using the appropriate tag to locate the title and price
    title  = soup.find('h1', class_='product-title').text.strip()
    price = soup.find('span', class_="product-price").text.srip()
    
    
    #printing the extracted  information
    print(f'Title:{title}')
    print(f'Price:{price}')
else:
    print(f'Failed to  retrieve the page. Status cod:{response.status_code}')    
    
    
    
    #  Write a Python program that scrapes the headlines and summaries
    # of the latest news 
    # articles from a news website. Print the extracted information   

url  =   'https://www.example-news-website.com'

response  = requests.get(url)


if response.status_code == 200:
# parse the html content of the page using BeautifulSoup

  soup = BeautifulSoup(response.text, 'html.parser')
  
  
#using appropiate  tag to locate   headline and summaries
headlines  = soup.find_all('h2', class_='headline-class')
summaries  =  soup.find_all('p', class_='summary-class')


for i in range(len(headlines)):
        headline = headlines[i].text.strip()
        summary = summaries[i].text.strip()
        print(f'Headline: {headline}')
        print(f'Summary: {summary}')
        print('-' * 30)  # Add a separator for readability
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')

    