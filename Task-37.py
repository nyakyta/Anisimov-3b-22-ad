cnt = int(input())
lst = []
for i in range(cnt):
    cur = int(input())
    lst.append(cur)
try:
    print(sorted(lst)[0], sorted(lst)[1])
except IndexError:
    print('В списке меньше двух символов')
