todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '2':
        print("\nTasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
