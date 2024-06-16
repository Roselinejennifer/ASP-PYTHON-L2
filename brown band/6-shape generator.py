import json
import os

# Directory to store shape definitions
SHAPE_DIR = 'shape_definitions'

# Ensure the shape directory exists
if not os.path.exists(SHAPE_DIR):
    os.makedirs(SHAPE_DIR)

class ShapeGenerator:
    def __init__(self):
        self.shapes = {}

    def add_shape(self, name, points):
        self.shapes[name] = points
        self.save_shapes()

    def remove_shape(self, name):
        if name in self.shapes:
            del self.shapes[name]
            self.save_shapes()
            print(f"Shape '{name}' removed successfully.")
        else:
            print(f"Shape '{name}' not found.")

    def draw_shape(self, name):
        if name in self.shapes:
            print(f"Drawing shape '{name}': {self.shapes[name]}")
            # Code to draw the shape based on its points
        else:
            print(f"Shape '{name}' not found.")

    def save_shapes(self):
        with open(os.path.join(SHAPE_DIR, 'shapes.json'), 'w') as file:
            json.dump(self.shapes, file, indent=4)

    def load_shapes(self):
        shapes_file = os.path.join(SHAPE_DIR, 'shapes.json')
        if os.path.exists(shapes_file):
            with open(shapes_file, 'r') as file:
                self.shapes = json.load(file)

def display_menu():
    print("\nShape Generator Menu")
    print("1. Add Shape")
    print("2. Remove Shape")
    print("3. Draw Shape")
    print("4. Exit")

def shape_generator_app():
    shape_generator = ShapeGenerator()
    shape_generator.load_shapes()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter shape name: ")
            points = input("Enter shape points (comma-separated): ").split(',')
            shape_generator.add_shape(name, points)
        elif choice == '2':
            name = input("Enter shape name to remove: ")
            shape_generator.remove_shape(name)
        elif choice == '3':
            name = input("Enter shape name to draw: ")
            shape_generator.draw_shape(name)
        elif choice == '4':
            print("Exiting the shape generator.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the shape generator application
if __name__ == "__main__":
    shape_generator_app()
