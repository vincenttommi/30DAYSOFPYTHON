# Write a Python program that reads the content of the JSON file and prints it on the console

import json 
 
with open('Day14/data.json','r')  as file:
    data  = json.load(file)
      
    print(data)




with open('Day14/books.json','r') as file:
    
    books = json.load(file)
    
#iterating over  each book and printing the title and author

for book in  books:
    
    # author = book['author']: This line assigns the value of the 'author' key from the book dictionary to the variable author. It retrieves the author information of the current book.
    title  =  book['title']
    author  = book['author']
    
    print("Title:", title)
    print("Author:", author)
    
    print()
    
    # for printing all
    # print(book)