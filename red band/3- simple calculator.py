class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Integer(Number):
    def __init__(self, value):
        super().__init__(int(value))

class Float(Number):
    def __init__(self, value):
        super().__init__(float(value))

class Complex(Number):
    def __init__(self, real, imag):
        super().__init__(complex(real, imag))

class Operation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Addition(Operation):
    def execute(self):
        return self.left.value + self.right.value

class Subtraction(Operation):
    def execute(self):
        return self.left.value - self.right.value

class Multiplication(Operation):
    def execute(self):
        return self.left.value * self.right.value

class Division(Operation):
    def execute(self):
        if self.right.value == 0:
            raise ValueError("Cannot divide by zero")
        return self.left.value / self.right.value

def calculate(operation):
    return operation.execute()

def display_result(result):
    print("Result:", result)

def main():
    # Integer addition
    num1 = Integer(5)
    num2 = Integer(3)
    addition = Addition(num1, num2)
    result = calculate(addition)
    display_result(result)

    # Float division
    num3 = Float(10.5)
    num4 = Float(2.5)
    division = Division(num3, num4)
    result = calculate(division)
    display_result(result)

    # Complex number multiplication
    num5 = Complex(2, 3)
    num6 = Complex(1, -4)
    multiplication = Multiplication(num5, num6)
    result = calculate(multiplication)
    display_result(result)

    # Subtraction of integers
    num7 = Integer(10)
    num8 = Integer(4)
    subtraction = Subtraction(num7, num8)
    result = calculate(subtraction)
    display_result(result)  

if __name__ == "__main__":
    main()
