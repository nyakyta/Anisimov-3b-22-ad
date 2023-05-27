try:
    file = open('test.txt', 'r')
    file.close()
    print('Файл существует')
except FileNotFoundError:
    print('Файл не найден')
