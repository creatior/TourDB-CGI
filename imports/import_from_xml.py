import sqlite3
from xml.dom import minidom
import os

db_path = os.path.join(os.getcwd(), './db/tours.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def import_from_xml(table_name, file_name):
    doc = minidom.parse(file_name)
    rows = doc.getElementsByTagName('row')

    cursor.execute(f'PRAGMA table_info({table_name})')
    columns = [column[1] for column in cursor.fetchall()]

    for row in rows:
        values = []
        for col_name in columns:
            col_elem = row.getElementsByTagName(col_name)[0]
            col_value = col_elem.firstChild.nodeValue
            values.append(col_value)
        placeholders = ', '.join(['?'] * len(values))
        cursor.execute(f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})', values)

    conn.commit()

import_from_xml('tour', 'xmls/tour.xml')
import_from_xml('client', 'xmls/client.xml')
import_from_xml('booking', 'xmls/booking.xml')

conn.close()