import abc

# metaclass=abc.ABCMetaと書くことで抽象クラスであることを示す
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1) -> None:
        self.age = age

    # selfはオブジェクト自身を指す引数
    def say_something(self):
        print("I am {}".format(self.name))
        self.run(10)

    def run(self, num):
        print("run" * num)

    def __del__(self):
        print("good bye")

    # driveメソッドを継承先のクラスで必ず実装するように指定
    # この状態で継承先クラスのオブジェクトをせ生したとき,driveメソッドがないとエラーになる
    @abc.abstractclassmethod
    def drive(self):
        pass
        # if self.age >= 18:
        #     print("OK")
        # else:
        #     raise Exception("No drive")


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18) -> None:
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    
    def drive(self):
        print('ok')
    
