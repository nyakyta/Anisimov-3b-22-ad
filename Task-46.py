try:
    file = open('test.txt', 'w')
    file.write('Hello, world!\n')
    file.close()
except Exception:
    print('Ошибка')
