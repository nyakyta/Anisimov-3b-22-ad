cnt_glasn = 0
cnt_sogl = 0
str_ = input()
for sym in str_.lower():
    if sym in "аиеёоуыэюяaeiouy":
        cnt_glasn += 1
    elif sym in "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz":
        cnt_sogl += 1

print(cnt_glasn, cnt_sogl)
