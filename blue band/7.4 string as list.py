my_string = "Hello, World!"

# Convert string to list of characters
char_list = list(my_string)
print("List of characters:", char_list)

# Accessing individual characters
first_char = char_list[0]
print("First character:", first_char)

# Slicing the string (list)
substring = char_list[7:12]
print("Substring from index 7 to 11:", "".join(substring))

# Modifying characters in the list
char_list[7] = 'w'
char_list[8] = 'o'
char_list[9] = 'r'
char_list[10] = 'l'
char_list[11] = 'd'
modified_string = "".join(char_list)
print("Modified string:", modified_string)

# Joining the list back into a string
joined_string = "".join(char_list)
print("Joined string:", joined_string)

# Iterating over the string (list)
for char in char_list:
    print(char, end=' ')
print()

# Checking if a character is in the string (list)
if 'H' in char_list:
    print("'H' is in the list")
else:
    print("'H' is not in the list")

# Finding the length of the string (list)
length = len(char_list)
print("Length of the string (list):", length)
