import sqlite3
import json
import os

db_path = os.path.join(os.getcwd(), './db/tours.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def export_to_json(table_name, file_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    data = []
    for row in rows:
        row_dict = {col_name: col_value for col_name, col_value in zip(columns, row)}
        data.append(row_dict)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

export_to_json('tour', 'jsons/tour.json')
export_to_json('client', 'jsons/client.json')
export_to_json('booking', 'jsons/booking.json')

conn.close()
