from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define the database connection and session
DATABASE_URL = "sqlite:///books_authors.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the BookAuthor association table
book_author_association = Table(
    'book_author_association',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

# Define the Author table
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", secondary=book_author_association, back_populates="authors")

# Define the Book table
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    authors = relationship("Author", secondary=book_author_association, back_populates="books")

# Create tables in the database
Base.metadata.create_all(engine)

# Insert data into the tables
author1 = Author(name='J.R.R. Tolkien')
author2 = Author(name='iqwaston')
author3 = Author(name='vincenttmmi')
author4 = Author(name='Rong Rende')
author5 = Author(name='Dan Karanja')




book1 = Book(title='The Lord of the Rings')
book2 = Book(title='A Song of Ice and Fire')
book3 = Book(title='48 laws of power')
book4 = Book(title='Rich Dad ,Poor Dad')
book5 = Book(title='The way of the superior man')




book1.authors.append(author1)
book2.authors.append(author2)
book3.authors.append(author3)
book4.authors.append(author4)
book5.authors.append(author5)




session.add(author1)
session.add(author2)
session.add(author3)
session.add(author4)
session.add(author5)



session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)




session.commit()

# Query for books by a specific author

