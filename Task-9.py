class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_square(self):
        return self.width * self.height


ex_rect = Rectangle(1, 2)
print(ex_rect.height, ex_rect.width, ex_rect.get_square())
