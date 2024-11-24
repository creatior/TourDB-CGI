#!/usr/bin/env python3

import sqlite3
import cgi
import os

print("Content-Type: text/html\n")

db_path = os.path.join(os.getcwd(), './db/tours.db')

con = sqlite3.connect(db_path)
cur = con.cursor()
form = cgi.FieldStorage()

tour_name = form.getvalue("tour_name")
description = form.getvalue("description")
duration = form.getvalue("duration")
price = form.getvalue("price")

cur.execute('''INSERT INTO tour (tour_name, description, duration, price)
                VALUES (?, ?, ?, ?)''',
            (tour_name, description, duration, price))

con.commit()
con.close()

print('<a href="../forms/tour_form.html">Вернуться к форме</a>')