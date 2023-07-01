import sqlite3


conn = sqlite3.connect('database_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title TEXT, genre TEXT, rate REAL)''')
titles = ['Мальчишник в Вегасе 1', 'Паразиты', 'Всё везде и сразу', 'Майор Пэйн', 'Аватар', 'Война миров']
genres = ['Комедия', 'Драма', 'Фантастика', 'Комедия', 'Фантастика', 'Фантастика']
rates = [7.9, 8.0, 7.2, 7.6, 8.0, 7.1]
for i in range(len(titles)):
    cursor.execute("INSERT INTO films (id, title, genre, rate) VALUES (?, ?, ?, ?)", (i + 1, titles[i], genres[i], rates[i]))
conn.commit()

cursor.execute('''select * from films where genre = 'Фантастика' ''')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
