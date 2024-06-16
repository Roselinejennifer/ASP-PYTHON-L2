def is_prime(num):
   if num < 2:
       return False
   for i in range(2, num):
       if num % i == 0:
           return False
   return True
num = int(input("Enter a number: "))
is_prime = is_prime(num)
if is_prime:
   print(num, "is a prime number.")
else:
   print(num, "is not a prime number.")