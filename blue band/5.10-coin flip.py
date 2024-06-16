import random
num_flips = int(input("enter the number of coin flips:"))
coin_flip_results = (random.choice(['Heads','Tails'])for _ in range(num_flips))
print("Results:")
for result in coin_flip_results:
    print(result)