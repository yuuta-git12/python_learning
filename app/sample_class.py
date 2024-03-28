import Person
import Car

# Person.pyにあるクラスPersonクラスを使いたい場合の書き方
# Personクラスのオブジェクトを作成
person = Person.Person('Mike')
# オブジェクトからメソッドsay_something()を呼び出す

print('############')

person.say_something()


car = Car.Car('normal')
car.run()
print('############')
mycar = Car.MyCar('sedan')
mycar.run()
print('############')
advanced_car = Car.AdvancedCar('SUV')
advanced_car.run()
advanced_car.auto_run()
print('############')

print(mycar.model)
print(advanced_car.model)
advanced_car.enable_auto_run = True
# print(advanced_car.enable_auto_run)