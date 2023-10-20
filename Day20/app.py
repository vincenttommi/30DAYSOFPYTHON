from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Creating a database connection
DATABASE_URL = "sqlite:///database.db"  # Use triple slash for SQLite
engine = create_engine(DATABASE_URL)

# Creating a session factory using sessionmaker function
Session = sessionmaker(bind=engine)

# Using the session factory to create individual sessions that
# will be used to interact with the database
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    # Establishing the reverse relationship to tasks
    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))  
    # Corrected ForeignKey usage

    # Establish the relationship to the user model
    user = relationship("User", back_populates="tasks")

# Create the tables in the database
Base.metadata.create_all(engine)

# Creating User and Task objects and adding them to the session
user = User(username="vincenttommi", email="vincenttommi@gmail.com")
task = Task(title="Complete project", user=user)  # Assign the user object, not string
user = User(username="DanielKarnaj", email="skaranja@gmail.com")
task = Task(title="Coding Backend-Development", user=user)
user = User(username="kencoder", email="ken@gmail.com")
task = Task(title="Fullstack-Developer", user=user)

session.add(user)
session.add(task)
session.commit()

#retrieving data using sqlalchemy
users =  session.query(User).all()

#Retrieve a single user by id
user = session.query(User).get(1)


#filtering and  sorting query  results  with sqlalchemy
# users = session.query(User).filter_by(email="vincenttommi@gmail.com").all()


#Retreive users whose  usernames start with 'j and sort by username
# users = session.query(User).filter(User.username.startswith("j")).order_by(User.username).all()


# updating Data(in CRUD)
#steps
"""
1 Query the record I need to update
2 Modify the attributes of  queried object
3  Commit  session to save changes to database
"""

# Query a user by id
user =  session.query(User).get(2)


#updating the user's email
user.email = "vincent@gmail.com"


# committing the changes
session.commit()




#Deleting Data in (CRUD)
"""steps


Query the record you want to delete
Use session's delete method to remove the object
Commit  session to finalize deletion

"""

#Querying a user  by id
user = session.query(User).get(6)
user = session.query(User).get(7)


#Delete the user

session.delete(user)
session.commit()