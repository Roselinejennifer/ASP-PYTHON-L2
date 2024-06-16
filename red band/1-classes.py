class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("Woof!")

# Creating instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")

# Using the methods
print(dog)
print(dog.speak())

