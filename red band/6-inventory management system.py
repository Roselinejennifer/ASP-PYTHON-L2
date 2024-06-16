class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

class Order:
    def __init__(self, items, customer):
        self.items = items
        self.customer = customer
        self.total_price = sum(item.price * item.quantity for item in items)

class InventoryManagementSystem:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added.")

    def update_product(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.update_quantity(new_quantity)
                print(f"Product '{product_name}' quantity updated to {new_quantity}.")
                break
        else:
            print(f"Product '{product_name}' not found.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' removed.")
                break
        else:
            print(f"Product '{product_name}' not found.")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer '{customer.name}' added.")

    def remove_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                self.customers.remove(customer)
                print(f"Customer '{customer_name}' removed.")
                break
        else:
            print(f"Customer '{customer_name}' not found.")

# Sample usage
if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()

    # Add products
    product1 = Product("Laptop", "Gaming laptop", 1200, 10)
    product2 = Product("Phone", "Smartphone", 800, 20)
    inventory_system.add_product(product1)
    inventory_system.add_product(product2)

    # Update product quantity
    inventory_system.update_product("Laptop", 8)

    # Remove product
    inventory_system.remove_product("Phone")

    # Add customers
    customer1 = Customer("Alice", "123 Main St")
    customer2 = Customer("Bob", "456 Oak St")
    inventory_system.add_customer(customer1)
    inventory_system.add_customer(customer2)

    # Remove customer
    inventory_system.remove_customer("Bob")
