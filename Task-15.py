class Auto:

    def __init__(self, mark, model, year, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.price = price

    def get_info(self):
        print(f'{self.mark} - {self.model}, {self.year}, {self.price}')


auto = Auto('Volkswagen', 'Polo', '2020', 1000000)
auto.get_info()
