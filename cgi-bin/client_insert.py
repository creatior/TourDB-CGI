#!/usr/bin/env python3

import sqlite3
import cgi
import os

print("Content-Type: text/html\n")

db_path = os.path.join(os.getcwd(), './tours.db')

con = sqlite3.connect(db_path)
cur = con.cursor()
form = cgi.FieldStorage()

surname = form.getvalue("surname")
first_name = form.getvalue("first_name")
last_name = form.getvalue("last_name")
email = form.getvalue("email")
phone_number = form.getvalue("phone_number")

cur.execute('''INSERT INTO client (first_name, surname, last_name, email, phone_number)
                VALUES (?, ?, ?, ?, ?)''',
            (first_name, surname, last_name, email, phone_number))

con.commit()
con.close()

print('<a href="../forms/client_form.html">Вернуться к форме</a>')