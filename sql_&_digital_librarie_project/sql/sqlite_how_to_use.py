#import sqlite3
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, URL


### SQLlite stuff ###

# db = sqlite3.connect("all_books.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books "
# #                "(id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL, "
# #                "author varchar(250) NOT NULL, "
# #                "rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1,'Harry potter', 'jk rowling', '7.0')")
# db.commit()


### SQLAlchemy ###
url_ = URL.create(drivername="database_practise",
                  username="Dread",
                  password="76102005",
                  database="all_new_books")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db.init_app(app)


class New_Books(db.Model):
    id: Mapped[int] = mapped_column(name="id", primary_key=True)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(unique=True, nullable=False)

# with app.app_context():
#     db.session.add(1)
#     db.session.add("JK rowling")
#     db.session.add("Harry pitcher")
#     db.session.add(3.1)
#     db.session.execute()


with app.app_context():
    book = db.session.execute(db.select(New_Books).where(New_Books.title == "Harry pitcher")).scalar()
# with app.app_context():
#     db.create_all()




