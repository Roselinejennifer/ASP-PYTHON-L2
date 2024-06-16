class Car:
    def __init__(self, make, model, year, color, type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

        self.type = type


    def accelerate(self):

        print(f"{self.make} {self.model} accelerates!")


    def brake(self):

        print(f"{self.make} {self.model} brakes!")


    def turn(self, direction):

        print(f"{self.make} {self.model} turns {direction}.")


    def get_info(self):

        info = f"{self.year} {self.color} {self.make} {self.model} ({self.type})"

        return info



class Sedan(Car):

    def __init__(self, make, model, year, color):

        super().__init__(make, model, year, color, "Sedan")


    def __str__(self):

        return f"Sedan: {self.get_info()}"



class SportsCar(Car):

    def __init__(self, make, model, year, color):

        super().__init__(make, model, year, color, "Sports Car")


    def accelerate(self):

        print(f"{self.make} {self.model} zooms ahead!")


    def __str__(self):

        return f"Sports Car: {self.get_info()}"



# Create car instances

honda_accord = Sedan("Honda", "Accord", 2023, "Silver")

porsche_911 = SportsCar("Porsche", "911", 2022, "Red")


# Call methods

honda_accord.accelerate()

porsche_911.brake()
porsche_911.turn("left")


# Print car information

print(honda_accord)

print(porsche_911)



