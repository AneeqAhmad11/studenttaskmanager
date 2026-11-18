
from task_manager import TaskManager

manager = TaskManager()


def show_menu():
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")

        try:
            task_id = manager.add_task(title)
            print(f"Task added successfully! ID: {task_id}")

        except ValueError as error:
            print(error)

    elif choice == "2":
        tasks = manager.display_tasks()

        if not tasks:
            print("No tasks available.")

        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"

            print(
                f'ID: {task["id"]} | '
                f'Task: {task["title"]} | '
                f'Status: {status}'
            )

    elif choice == "3":
        try:
            task_id = int(input("Enter task ID: "))

            if manager.complete_task(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found or already completed.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            task_id = int(input("Enter task ID: "))

            if manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Try again.")
