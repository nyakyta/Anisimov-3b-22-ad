class GeometryFigure:

    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def get_info(self):
        print(f'площадь - {self.square}, периметр - {self.perimeter}')


rectangle = GeometryFigure(50, 15)
rectangle.get_info()
