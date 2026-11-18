
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

    # Add Task
    if choice == "1":

        title = input("Enter task title: ")

        try:
            task_id = manager.add_task(title)
            print(f"Task added successfully! ID: {task_id}")

        except ValueError as error:
            print(error)

    # Display Tasks
    elif choice == "2":

        tasks = manager.display_tasks()

        if not tasks:
            print("No tasks available.")

        else:
            for task in tasks:

                status = "Completed" if task["completed"] else "Pending"

                print(
                    f'ID: {task["id"]} | '
                    f'Task: {task["title"]} | '
                    f'Status: {status}'
                )

    # Complete Task
    elif choice == "3":

        try:
            task_id = int(input("Enter task ID: "))

            tasks = manager.display_tasks()

            selected_task = next(
                (task for task in tasks if task["id"] == task_id),
                None
            )

            if selected_task is None:
                print("Task ID not found.")

            elif selected_task["completed"]:
                print("This task is already completed.")

            elif manager.complete_task(task_id):
                print("Task marked as completed.")

        except ValueError:
            print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":

        try:
            task_id = int(input("Enter task ID: "))

            if manager.delete_task(task_id):
                print("Task deleted successfully.")

            else:
                print("Task ID not found.")

        except ValueError:
            print("Please enter a valid number.")

    # Exit
    elif choice == "5":

        print("Thank you for using Student Task Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
