from random import randrange
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from faker import Faker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import server

# app
app = Flask(__name__)

# config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()

faker = Faker()

# create dummy users
for i in range(200):
    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'
    new_user = server.User(name=name, address=address, phone=phone, email=email)
    db.session.add(new_user)
    db.session.commit()

# create dummy blog posts
for i in range(200):
    title = faker.sentence(5)
    body = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 200)

    new_blog_post = server.BlogPost(
        title=title, body=body, date=date, user_id=user_id
    )
    db.session.add(new_blog_post)
    db.session.commit()

