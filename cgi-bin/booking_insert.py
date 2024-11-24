#!/usr/bin/env python3

import sqlite3
import cgi
import os

print("Content-Type: text/html\n")

db_path = os.path.join(os.getcwd(), './tours.db')

con = sqlite3.connect(db_path)
cur = con.cursor()
form = cgi.FieldStorage()

client_id = form.getvalue("client_id")
tour_id = form.getvalue("tour_id")
booking_date = form.getvalue("booking_date")

cur.execute('''INSERT INTO booking (client_id, tour_id, booking_date)
                VALUES (?, ?, ?)''',
            (client_id, tour_id, booking_date))

con.commit()
con.close()

print('<a href="../forms/booking_form.html">Вернуться к форме</a>')