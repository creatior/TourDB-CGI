#!/usr/bin/env python3

import cgi
import cgitb
import sqlite3
import os

print("Content-Type: text/html\n")
cgitb.enable()

db_path = os.path.join(os.getcwd(), './db/tours.db')

def get_bookings_info():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT
                        tour.tour_name, booking.booking_date, client.surname, client.first_name, client.last_name
                        FROM
                        booking JOIN client
                        ON
                        booking.client_id = client.client_id
                        JOIN tour
                        ON
                        booking.tour_id = tour.tour_id''')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_tours_info():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT tour_name, description, duration, price FROM tour")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_clients_info():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT surname, first_name, last_name, email, phone_number FROM client")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# Функция для генерации HTML-страницы
def generate_html(tours, bookings, clients):
    print()
    print("<html>")
    print("<head><title>Данные таблиц</title></head>")
    print("<body>")
    print("<h1>Экскурсии</h1>")
    print("<table border='1'>")
    print("<tr><th>Название</th><th>Описание</th><th>Длительность</th><th>Цена</th></tr>")
    for tour in tours:
        print(f"<tr><td>{tour[0]}</td><td>{tour[1]}</td><td>{tour[2]}</td><td>{tour[3]}</td></tr>")
    print("</table>")
    print("<h1>Клиенты</h1>")
    print("<table border='1'>")
    print("<tr><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Электронная почта</th><th>Номер телефона</th></tr>")
    for client in clients:
        print(f"<tr><td>{client[0]}</td><td>{client[1]}</td><td>{client[2]}</td><td>{client[3]}</td><td>{client[4]}</td></tr>")
    print("</table>")
    print("<h1>Бронирования</h1>")
    print("<table border='1'>")
    print("<tr><th>Название экскурсии</th><th>Дата бронирования</th><th>Фамилия</th><th>Имя</th><th>Отчество</th></tr>")
    for booking in bookings:
        print(f"<tr><td>{booking[0]}</td><td>{booking[1]}</td><td>{booking[2]}</td><td>{booking[3]}</td><td>{booking[4]}</td></tr>")
    print("</table>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    tours = get_tours_info()
    bookings = get_bookings_info()
    clients = get_clients_info()
    generate_html(tours, bookings, clients)
