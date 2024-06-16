# Open the file in read mode
file_path = "file.txt"  # Replace "file.txt" with the path to your file
try:
    with open(file_path, "r") as file:

        file_contents = file.read()

        print(file_contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Could not read from file '{file_path}'.")

