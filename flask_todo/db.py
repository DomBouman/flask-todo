#Import library
import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

#Connect using psycopg2
conn = psycopg2.connect("dbname=todoapp host=localhost")

#Activate connection cursor
cur = conn.cursor()

#Select table and display
cur.execute("SELECT name, completed, date_added")
rows = cur.fetchall()
rows

#Insert entry
cur.execute("INSERT INTO todo_items (name, completed, date_added) VALUES (%s, %s, %s)", (name, False, date))
conn.commit()


#Close Connection
cur.close()
conn.close()
