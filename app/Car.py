class Car(object):
    def __init__(self, model=None) -> None:
        self.model = model

    def run(self):
        print("run")


class MyCar(Car):
    def run(self):
        print("fast")


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False) -> None:
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    def auto_run(self):
        print("auto run")

    def run(self):
        print("super fast")

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
