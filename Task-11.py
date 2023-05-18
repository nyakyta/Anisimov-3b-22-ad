class Dog:

    def __init__(self, name, breed, ages):
        self.name = name
        self.breed = breed
        self.ages = ages

    def get_info(self):
        print(f'Имя: {self.name}')
        print(f'Порода: {self.breed}')
        print(f'Возраст: {self.ages}')


dog = Dog('Стрелка', 'ротвейлер', 3)
dog.get_info()
