# Write a Python program that reads the content of the JSON file and prints it on the console

import json 
 
with open('Day14/data.json','r')  as file:
    data  = json.load(file)
      
    print(data)
