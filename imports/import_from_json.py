import sqlite3
import json
import os

db_path = os.path.join(os.getcwd(), './db/tours.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def import_from_json(table_name, file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cursor.execute(f'PRAGMA table_info({table_name})')
    columns = [column[1] for column in cursor.fetchall()]

    for row in data:
        values = [row[col_name] for col_name in columns]
        placeholders = ', '.join(['?'] * len(values))
        cursor.execute(f'INSERT OR REPLACE INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})', values)

    conn.commit()

import_from_json('tour', 'jsons/tour.json')
import_from_json('client', 'jsons/client.json')
import_from_json('booking', 'jsons/booking.json')

conn.close()