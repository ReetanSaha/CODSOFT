import os

# Path to tasks.txt (always uses the file in the same folder as this script)
FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.txt")


# Function to load tasks from file
def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


# Function to save tasks to file
def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Display all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\n===== YOUR TASKS =====")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


# Add a new task
def add_task(tasks):
    task = input("Enter new task: ").strip()

    if task == "":
        print("Task cannot be empty.\n")
        return

    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added successfully!\n")


# Mark a task as completed
def complete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            if tasks[number - 1].startswith("[ ]"):
                tasks[number - 1] = tasks[number - 1].replace("[ ]", "[✓]", 1)
                save_tasks(tasks)
                print("Task marked as completed!\n")
            else:
                print("Task is already completed.\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Delete a task
def delete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed_task}\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("========== TO-DO LIST ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


# Run the program
if __name__ == "__main__":
    main()