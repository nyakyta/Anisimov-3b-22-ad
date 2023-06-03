def sum_square(cur_tuple):
    return cur_tuple[0] ** 2 + cur_tuple[1] ** 2


lst = [(1, 2), (3, 4), (-1, 5), (6, -3)]
print(sorted(lst, key=sum_square))
