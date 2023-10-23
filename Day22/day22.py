"""


 Write a Python program that scrapes the names, prices, and ratings of all products in a specific category on an e-commerce website, handling pagination. Print the extracted information.

"""
import requests
from bs4 import BeautifulSoup


def scrape_category(url):
    page_no = 1
    products = []
    
    
    
    while True:
        #Construct the  URL for the current page with pagination
        page_url = "f{url}?page={page_number}"
        response = requests.get(page_url)
        
        
        
         #checking the response of the page
        if response.status_code != 200:
            break   #stop is the page doen't exist
        
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        #Find and  extract  product information based on HTML Structure
        products_I =  soup.find_all('div', class_='product-item') #
        #updating  with correct HTML structure
        
        #looping products items
        for item in products_I:
            
            name = item.find('h2', class_='product-name').text
            price = item.find('h2', class_='product-price').text
            rating = item.find('h2', class_='product-rating').text 
            
            
            #appending values to our list
            products.append({
                
                'name':name,
                'price':price,
                'rating':rating
            })
            
            #Incrementing the  number of pages  for the next page
            page_no  += 1
            
            
        if __name__ == "__main__":
            category_url = 'https://www.example.com/category'
            
            scraped_data = scrape_category(category_url)
            
            for data in scraped_data:
                print(f"Name:{product['name']}")
                print(f"Price:{product['price']}")
                print(f"Rating:{product['rating']}")
                print()
                
                
                
    
    

