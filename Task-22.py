from random import randint
lst = [randint(1, 10) for i in range(10)]
summary = 0
for elem in lst:
    summary += elem
print(lst)
print(summary)
