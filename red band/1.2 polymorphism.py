def make_sound(thing):

    thing.speak()  

class Dog:

    def speak(self):

        print("Woof!")

class Cat:

    def speak(self):

        print("Meow!")


make_sound(Dog())

make_sound(Cat())