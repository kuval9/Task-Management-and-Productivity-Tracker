# TASK MANAGER by - Kuval Dayal (25BAI11610)


from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n=== TASK MANAGEMENT SYSTEM ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            manager.add_task(task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_num = int(input("Enter task number to mark completed: "))
            manager.complete_task(task_num)

        elif choice == "4":
            task_num = int(input("Enter task number to delete: "))
            manager.delete_task(task_num)

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()