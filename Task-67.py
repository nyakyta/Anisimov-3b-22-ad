import sqlite3


conn = sqlite3.connect('database_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)''')
titles = ['Горе от ума', 'Евгений Онегин', 'Перси Джексон и похититель молний', 'Стив Джобс', 'Война и мир']
authors = ['Грибоедов', 'Пушкин', 'Риордан', 'Айзексон', 'Толстой']
years = [1825, 1825, 2005, 2011, 1867]
for i in range(len(titles)):
    cursor.execute("INSERT INTO books (id, title, author, year) VALUES (?, ?, ?, ?)", (i + 1, titles[i], authors[i], years[i]))
conn.commit()

cursor.execute('''select * from books where year > 2000''')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()