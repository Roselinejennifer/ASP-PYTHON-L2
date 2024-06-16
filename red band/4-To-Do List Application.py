import json

class ToDoList:
    def __init__(self, filename='todolist.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save_tasks()
        else:
            print("Invalid task number")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task number")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        for i, task in enumerate(self.tasks):
            status = "✔" if task["completed"] else "✖"
            print(f"{i + 1}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
