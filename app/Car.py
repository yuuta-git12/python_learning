class Car(object):
    def __init__(self, model=None) -> None:
        self.model = model

    def run(self):
        print("run")
    
    def ride(self, person):
        person.drive()


class MyCar(Car):
    def run(self):
        print("fast")


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False,password='123') -> None:
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.password = password

    def auto_run(self):
        print("auto run")

    def run(self):
        print("super fast")

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '345':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError
