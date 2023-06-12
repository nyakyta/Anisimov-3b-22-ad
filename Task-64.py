class Bank:
    def __init__(self):
        self.clients_names = []
        self.clients_accounts = {}
        self.accounts = [1]
        self.clients_transactions = []
        self.accounts_money = {}

    def add_client(self, client_name):
        self.clients_names.append(client_name)

    def open_account(self, client_name, deposit=0):
        self.clients_accounts[client_name] = self.accounts[len(self.accounts) - 1] + 1
        self.accounts.append(self.accounts[len(self.accounts) - 1] + 1)
        self.accounts_money[
            self.clients_accounts[client_name]] = deposit

    def transaction(self, from_name, to_name, sum_dep):
        from_account = self.clients_accounts[from_name]
        to_account = self.clients_accounts[to_name]
        if self.accounts_money[from_account] >= sum_dep:
            self.accounts_money[from_account] -= sum_dep
            self.accounts_money[to_account] += sum_dep
            self.clients_transactions.append((from_account, to_account, sum_dep))
        else:
            print('Недостаточно средств')


sbank = Bank()
sbank.add_client('Oleg Gorodovoy')
sbank.add_client('Vyacheslav Bort')
sbank.open_account('Oleg Gorodovoy', 100)
sbank.open_account('Vyacheslav Bort', 50)
sbank.transaction('Oleg Gorodovoy', 'Vyacheslav Bort', 100)
print(sbank.clients_names,
      sbank.clients_accounts,
      sbank.accounts,
      sbank.clients_transactions,
      sbank.accounts_money)
