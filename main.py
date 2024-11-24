import sqlite3

con = sqlite3.connect("db/tours.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tour (
                    tour_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                    tour_name VARCHAR(150) NOT NULL,
                    description TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    price REAL NOT NULL
                 )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS client (
                    client_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                    first_name VARCHAR(40) NOT NULL,
                    surname VARCHAR(40) NOT NULL,
                    last_name VARCHAR(40) NOT NULL,
                    email VARCHAR(30) NOT NULL,
                    phone_number VARCHAR(15) NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS booking (
                    booking_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                    client_id INTEGER NOT NULL,
                    tour_id INTEGER NOT NULL,
                    booking_date DATE NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES client(client_id),
                    FOREIGN KEY (tour_id) REFERENCES tour(tour_id)
                 )''')

# Список экскурсий дороже 60.0 у. е.
cursor.execute("SELECT * FROM tour WHERE price >= 60.0")

select1 = cursor.fetchall()
print("Список экскурсий дороже 60.0 у. е.:\n{0}\n".format(select1))

# Список даты бронирования и клиентов позже 2023-10-03
cursor.execute('''SELECT 
               booking.booking_date, client.surname, client.first_name, client.last_name 
               FROM 
               booking JOIN client 
               ON 
               booking.client_id = client.client_id
               WHERE booking.booking_date >= "2023-10-03"''')

select2 = cursor.fetchall()
print("Список даты бронирования и клиентов позже 2023-10-03:\n{0}\n".format(select2))

# Список всех бронирований
cursor.execute('''SELECT
               client.surname, client.first_name, client.last_name, booking.booking_date, tour.tour_name
               FROM
               booking JOIN tour 
               ON booking.tour_id = tour.tour_id
               JOIN client
               ON booking.client_id = client.client_id''')
select3 = cursor.fetchall()
print("Список всех бронирований:\n{0}\n".format(select3))

con.commit()

print("Экскурсии:\n" + str(cursor.execute("SELECT * FROM tour").fetchall()) + "\n")
print("Клиенты:\n" + str(cursor.execute("SELECT * FROM client").fetchall()) + "\n")
print("Бронирования:\n" + str(cursor.execute("SELECT * FROM booking").fetchall()) + "\n")

con.close()