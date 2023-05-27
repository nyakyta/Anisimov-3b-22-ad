try:
    file = open('test.txt', 'r')
    text = file.read()
    print(text)
    file.close()
except FileNotFoundError:
    print('Файл не найден')
