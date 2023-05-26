str_ = input()
sym_frequency = {sym: str_.count(sym) for sym in str_}
print(sym_frequency)
