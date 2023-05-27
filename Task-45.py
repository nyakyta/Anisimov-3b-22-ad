file_name = input('Введите имя и расширение файла в формате name.extension\n\n')
try:
    file = open(file_name, 'r')
    text = file.read()
    print(text)
    file.close()
except Exception:
    print('Ошибка')
