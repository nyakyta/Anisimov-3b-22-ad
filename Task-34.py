for i in range(1, 11):
    j = 10
    for j in range(1, 11):
        print(i * j, end='    ')
    if j != 10:
        print(j)
    else:
        print()
