import random
num_rolls = int(input("enter the number of times to roll the die:"))
results = [random.randint(1,6) for _ in range(num_rolls)]
print("Results:",results)