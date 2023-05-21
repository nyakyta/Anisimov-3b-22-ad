from math import sqrt
num = int(input())
is_prime = True
for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        print('Число не является простым')
        break
if is_prime:
    print('Число является простым')
