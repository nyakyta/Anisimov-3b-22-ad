class BankAccount:

    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def add_money(self, rubles):
        self.balance += rubles

    def dec_money(self, rubles):
        self.balance -= rubles


student = BankAccount('Александр', 41231, 1000)
student.add_money(100)
student.dec_money(40)
print(student.balance)
