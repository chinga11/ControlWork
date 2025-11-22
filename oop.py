from turtle import Shape


class Person:
    def __init__(self):
        self.age = 0

    def set_age(self, age):
        self.age = age
        if self.age < 0:
            return print( "возраст не может быть ниже нуля")

    def get_age(self):
        return self.age

p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Должна быть ошибка или предупреждение

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bike is pedaling"

car = Car()
bike = Bicycle()

print(car.move())  # Вывод: Car is driving
print(bike.move())  # Вывод: Bicycle is pedaling

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94



