import sqlite3


conn = sqlite3.connect('database_4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary INT)''')
names = ['Олег', 'Петр', 'Владимир', 'Валентин', 'Никита', 'Татьяна', 'Мария']
positions = ['CEO', 'Менеджер по развитию', 'Менеджер по продажам', 'Инженер', 'Топ-менеджер', 'Бухгалтер', 'Аналитик']
salaries = [1000000, 800000, 100000, 110000, 900000, 150000, 200000]
for i in range(len(names)):
    cursor.execute("INSERT INTO employees (id, name, position, salary) VALUES (?, ?, ?, ?)", (i + 1, names[i], positions[i], salaries[i]))
conn.commit()

cursor.execute('''select * from employees where position like '%енеджер%' ''')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

