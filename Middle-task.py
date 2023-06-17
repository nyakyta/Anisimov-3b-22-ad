# Написать программу, которая принимает на вход строку и выводит на экран
# количество различных подстрок строки, начинающихся и заканчивающихся
# одним и тем же символом.

def search_count_subs(cur_str: str):
    symbol_subs = {sym: set() for sym in set(cur_str)}
    # Словарь, куда будем заносить строки, начинающиеся на sym
    for i in range(len(cur_str)):
        for j in range(i + 1, len(cur_str)):
            if cur_str[i] == cur_str[j]:
                symbol_subs[cur_str[i]].add(cur_str[i:j + 1])
    # Проход по все строке, поиск и добавление подстрок
    # с равными начальным и конечным символами
    ans = 0
    for subs in symbol_subs.values():
        ans += len(subs)
    # Считаем длины множеств, содержащих уникальные подстроки
    return ans


str_ = input()
print(search_count_subs(str_))
