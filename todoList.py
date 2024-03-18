tasks = []

def display_menu():
    print("1. Add Tasks.")
    print("2. List Tasks.")
    print("3. Mark Task as Done.")
    print("4. Exit.")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})

def list_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

def mark_task_done():
    list_tasks()
    task_number = int(input("Enter task number to mark as done: ")) - 1
    tasks[task_number]["done"] = True

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()