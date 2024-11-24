import sqlite3

con = sqlite3.connect('db/tours.db')
cursor = con.cursor()

cursor.execute('''INSERT INTO tour (tour_name, description, duration, price) VALUES
                    ('Городская экскурсия', 'Экскурсия по историческим местам города', 3, 50.00),
                    ('Природная экскурсия', 'Экскурсия по национальному парку', 5, 75.00),
                    ('Музейная экскурсия', 'Экскурсия по лучшим музеям города', 4, 60.00),
                    ('Гастрономическая экскурсия', 'Экскурсия по лучшим ресторанам и кафе', 3, 45.00)
                ''')

cursor.execute('''INSERT INTO client (first_name, surname, last_name, email, phone_number) VALUES
                    ('Иван', 'Иванов', 'Иванович', 'ivan@example.com', '89654447752'),
                    ('Анна', 'Петрова', 'Денисовна', 'anna@example.com', '89882318765'),
                    ('Петр', 'Сидоров', 'Ильич', 'petr@example.com', '86544521485'),
                    ('Мария', 'Кузнецова', 'Борисовна', 'maria@example.com', '88526459635')
                ''')

cursor.execute('''INSERT INTO booking (client_id, tour_id, booking_date) VALUES
                    (1, 1, '2023-10-01'),
                    (2, 2, '2023-10-02'),
                    (3, 3, '2023-10-03'),
                    (4, 4, '2023-10-04')
                ''')

con.commit()
con.close()