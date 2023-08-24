### Day 17: ORM and Python 

# Applying the concept of OOP with Python Data
# * Create Python objects using SQL database records.
# * Create SQL database records using Python objects.
#### Exercise
import sqlite3

conn = sqlite3.connect('30.db')
cursor = conn.cursor()

# conn.execute('''
#            CREATE TABLE IF NOT EXISTS users
#           ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT,[user_email]TEXT)
#            ''')

# conn.execute('''
#           INSERT INTO users (user_id, user_name,use_email)

#                 VALUES
#                 (1),
#                 (''vinecnt),
#                 ('vincenttommi@gmail.co),
                
#           ''')


cursor.execute("SELECT * FROM users")
records = cursor.fetchall()



class User:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        
    users = [User(record[0], record[1], record[2]) for record in records]   
    
    for user in users:
        print(f"Name:{user.name},Email:{user.email}")
        
        conn.close()