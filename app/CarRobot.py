class Person2(object):
    def talk(self):
        print('talk')
    
    def run(self):
        print('person_run')


class Car2(object):
    def run(self):
        print('car run')


class PersonCarRobot(Person2, Car2):
    def fly(self):
        print('fly')
    
    @staticmethod
    def about(year):
        print('about PersonCarRobot{}'.format(year))


PersonCarRobot.about(2000)
person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()