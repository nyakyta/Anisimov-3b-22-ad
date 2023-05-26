class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def studying(self):
        print(f'{self.name} из {self.grade} класса учится')


stud = Student('Валерий', 5)
stud.studying()
