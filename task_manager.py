
class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # Add a new task
    def add_task(self, title):

        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1

        return task["id"]

    # Display all tasks
    def display_tasks(self):
        return self.tasks

    # Mark a task as completed
    def complete_task(self, task_id):

        if type(task_id) is not int or task_id <= 0:
            return False

        for task in self.tasks:

            if task["id"] == task_id:

                if task["completed"]:
                    return False

                task["completed"] = True
                return True

        return False

    # Delete a task
    def delete_task(self, task_id):

        if type(task_id) is not int or task_id <= 0:
            return False

        for task in self.tasks:

            if task["id"] == task_id:
                self.tasks.remove(task)
                return True

        return False
