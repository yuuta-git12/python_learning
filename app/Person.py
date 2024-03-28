class Person(object):
    def __init__(self, name='Taro') -> None:
        self.name = name
        print('First')
        print(self.name)

    # selfはオブジェクト自身を指す引数
    def say_something(self):
        print('I am {}'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run'*num)
    
    def __del__(self):
        print('good bye')


