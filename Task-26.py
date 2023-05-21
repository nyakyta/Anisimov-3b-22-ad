first = 10
second = 25
min_compose = 1
for i in range(2, max(first, second)):
    if first % i == 0 and second % i == 0:
        min_compose = i
        break
if min_compose == 1:
    print('Числа взаимно просты')
else:
    print(min_compose)
