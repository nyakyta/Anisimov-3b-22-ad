class ProductCard:
    def __init__(self, product_name, cost, count):
        self.product_name = product_name
        self.cost = cost
        self.count = count

    def dec_count(self, delta=1):
        self.count = max(0, self.count - delta)

    def dec_cost(self, delta=1):
        self.cost = max(0, self.cost - delta)


product = ProductCard('Mirror', 100, 2)
product.dec_cost(50)
product.dec_count(3)
print(product.cost, product.count)
