class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")
# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")
# Cat also inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using the methods
dog.eat()
dog.bark()
cat.eat()
cat.meow()