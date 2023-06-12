from random import randint


class Person:
    def __init__(self, name, level, xp, damage, protection):
        self.name = name
        self.level = level
        self.xp = xp
        self.damage = damage
        self.protection = protection
        self.xp_before = xp

    def print_ch(self):
        print(self.name)
        print(self.level)
        print(self.xp)
        print(self.damage)
        print(self.protection)

    def more_power(self):
        self.level += 1
        self.xp *= 1.1

    def get_damage(self, damage):
        delta = self.protection - damage
        self.protection = max(0, delta)
        if delta < 0:
            self.xp = max(0, self.xp + delta)

    def renew_xp(self):
        self.xp = self.xp_before


first = Person('Chi', 1, 10, randint(2, 5), randint(3, 10))
second = Person('Cho', 1, 10, randint(2, 5), randint(3, 10))
first.print_ch()
second.print_ch()
for i in range(3):
    first.protection = randint(3, 10)
    second.protection = randint(3, 10)
    print(f'ROUND {i + 1}')
    while first.xp != 0 and second.xp != 0:
        first.get_damage(second.damage)
        second.get_damage(first.damage)
    if first.xp == 0 and second.xp == 0:
        first.renew_xp()
        second.renew_xp()
        print('There was draw')
    elif first.xp == 0:
        print(f'{second.name} win!')
        first.renew_xp()
        second.renew_xp()
        second.more_power()
    else:
        print(f'{first.name} win!')
        first.renew_xp()
        second.renew_xp()
        first.more_power()
print()
if first.level > second.level:
    print(f'{first.name} WIN!')
elif first.level < second.level:
    print(f'{second.name} WIN!')
else:
    print(f'DRAW!')
