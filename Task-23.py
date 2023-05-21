print('Введите число:')
num = int(input())
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    lst.index(num)
    print('Число найдено в массиве')
except ValueError:
    print('Число не найдено в массиве')
