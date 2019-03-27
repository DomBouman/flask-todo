#Import library
#import psycopg2

#Connect using psycopg2
#conn = psycopg2.connect("dbname=todoapp host=localhost")

#Activate connection cursor
#Cursor is making a link between the database and the app
#cur = conn.cursor()

#Insert entry
#cur.execute("INSERT INTO todo_items (name, completed, date_added) VALUES (%s, %s, %s)", (name, False, date))
#conn.commit()
