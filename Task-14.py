class Student:

    def __init__(self, name, surname, ages, spec):
        self.name = name
        self.surname = surname
        self.ages = ages
        self.spec = spec

    def get_info(self):
        print(f'{self.name} - {self.surname}, {self.ages} лет, {self.spec}')


student = Student('Владимир', 'Шварц', 40, 'аналитик')
student.get_info()
