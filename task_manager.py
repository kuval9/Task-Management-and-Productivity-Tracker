"""
Task Manager module
Author: Kuval Dayal
Reg No: 123456
Simple menu-based task manager.
"""




class TaskManager:
    def __init__(self):
        self.tasks = []   # Each task is stored as a dictionary

    def add_task(self, description):
        self.tasks.append({"desc": description, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for idx, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['desc']}  [{status}]")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")