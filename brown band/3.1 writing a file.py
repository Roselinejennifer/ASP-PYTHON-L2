# Define the content to write to the file
content = "Hello, world!\nThis is a sample text file."

# Specify the file path
file_path = "output.txt"

try:
    with open(file_path, "w") as file:

        file.write(content)
    print(f"Content has been written to '{file_path}' successfully.")
except IOError:
    print(f"Error occurred while writing to '{file_path}'.")
