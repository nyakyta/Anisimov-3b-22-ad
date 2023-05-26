cnt = int(input())
first = 1
second = 1
third = 1
if cnt <= 2:
    while cnt:
        print(first, end=' ')
        cnt -= 1
else:
    print(1)
    print(1)
    cnt -= 2
    while cnt:
        first = second
        second = third
        third = first + second
        cnt -= 1
        print(third, end=' ')
