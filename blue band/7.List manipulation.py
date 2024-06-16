my_list = [1, 2, 3, 4, 5]
print(my_list)

# append():
my_list.append(6)

# extend():
another_list = [7, 8, 9]
my_list.extend(another_list)

# insert():
my_list.insert(2, 10)

# remove():
my_list.remove(3)

# pop():
popped_element = my_list.pop(4)

# index():
index_of_4 = my_list.index(4)

# count():
count_of_2 = my_list.count(2)

# reverse():
my_list.reverse()

# sort():
my_list.sort()

# copy():
copied_list = my_list.copy()

# Using for Loop to Iterate Through a List
for item in my_list:
    print(item, end=' ')
print()

# Using enumerate with for Loop
for index, item in enumerate(my_list):
    print(f"Index: {index}, Value: {item}")

# Using while Loop with List
while my_list:
    print(my_list.pop(), end=' ')
print()



# Creating a List of Squares
squares = [x**2 for x in range(1, 6)]

# Filtering Even Numbers
even_numbers = [x for x in my_list if x % 2 == 0]

# Converting Strings to Uppercase
strings = ["hello", "world"]
uppercase_strings = [string.upper() for string in strings]

# Printing the modified lists and some additional information
print("Modified list:", my_list)
print("Popped element:", popped_element)
print("Index of 4:", index_of_4)
print("Count of 2:", count_of_2)
print("Copied list:", copied_list)
print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Uppercase strings:", uppercase_strings)
