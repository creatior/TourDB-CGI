import sqlite3
from xml.dom import minidom
import os

db_path = os.path.join(os.getcwd(), './db/tours.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def export_to_xml(table_name, file_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    doc = minidom.Document()
    root = doc.createElement(table_name)
    doc.appendChild(root)

    for row in rows:
        row_elem = doc.createElement('row')
        root.appendChild(row_elem)
        for col_name, col_value in zip(columns, row):
            col_elem = doc.createElement(col_name)
            col_elem.appendChild(doc.createTextNode(str(col_value)))
            row_elem.appendChild(col_elem)

    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  "))

export_to_xml('tour', 'xmls/tour.xml')
export_to_xml('client', 'xmls/client.xml')
export_to_xml('booking', 'xmls/booking.xml')

conn.close()
