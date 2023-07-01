import sqlite3
from random import randint


conn = sqlite3.connect('database_1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, avg_mark REAL)''')
names = ['James', 'Mate', 'Andrew', 'Jonh', 'Alexa', 'Jessica', 'William', 'Ivan', 'Oleg', 'Petr', 'Benedict']
ages = [randint(19, 25) for i in range(len(names))]
avg_marks = [randint(10, 100) / 10 for i in range(len(names))]
for i in range(len(names)):
    cursor.execute("INSERT INTO students (id, name, age, avg_mark) VALUES (?, ?, ?, ?)", (i + 1, names[i], ages[i], avg_marks[i]))
conn.commit()

cursor.execute('''select * from students''')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()