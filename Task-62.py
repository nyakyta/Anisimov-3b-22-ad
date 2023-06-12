class Robot:
    def __init__(self):
        self.name = 'Chappy'
        self.speed = 10

    def move(self, time):
        print(f'Робот {self.name} прошёл путь {time * self.speed}')


class CrawlerRobot(Robot):
    def __init__(self):
        Robot.__init__(self)
        self.territory = 'Moscow'


class WheelsRobot(Robot):
    def __init__(self):
        Robot.__init__(self)
        self.brand = 'MosRobot'


robot = Robot()
crawl = CrawlerRobot()
wheel = WheelsRobot()
robot.move(1)
crawl.move(5)
wheel.move(9)
print(crawl.territory)
print(wheel.brand)
