import sqlite3
import pandas  as pd

conn = sqlite3.connect('test.db') 
c = conn.cursor()

# c.execute('''
#           CREATE TABLE IF NOT EXISTS products
#           ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
#           ''')
          
# c.execute('''
#           CREATE TABLE IF NOT EXISTS prices
#           ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
#           ''')

# c.execute('''
#           INSERT INTO products (product_id, product_name)

#                 VALUES
#                 (1,'Computer'),
#                 (2,'Printer'),
#                 (3,'Tablet'),
#                 (4,'Desk'),
#                 (5,'Chair')
#           ''')
# c.execute('''
#           INSERT INTO prices (product_id, price)

#                 VALUES
#                 (1,800),
#                 (2,200),
#                 (3,300),
#                 (4,450),
#                 (5,150)
#           ''')

                     
                     
c.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a 
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')     

df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
print(df)                
conn.commit()