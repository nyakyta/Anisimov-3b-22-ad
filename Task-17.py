class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_info(self):
        print(f'{self.title}, {self.author} ({self.year}), {self.genre}')


book = Book('Войны 19 века', 'Булк', 1980, 'фантастика')
book.get_info()
