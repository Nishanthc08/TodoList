# Define an empty list to store tasks
tasks = []

# Function to display the menu options
def display_menu():
    print("1. Add Tasks.")
    print("2. List Tasks.")
    print("3. Mark Task as Done.")
    print("4. Exit.")

# Function to add a task to the list
def add_task():
    task = input("Enter task: ")
    # Append a dictionary representing the task with its status (done or not done)
    tasks.append({"task": task, "done": False})

# Function to list all tasks along with their status
def list_tasks():
    for index, task in enumerate(tasks, start=1):
        # Determine the status of the task (done or not done)
        status = "Done" if task["done"] else "Not Done"
        # Print the task along with its status
        print(f"{index}. {task['task']} - {status}")

# Function to mark a task as done
def mark_task_done():
    # Call the list_tasks function to display the list of tasks with their indices
    list_tasks()
    # Prompt the user to enter the index of the task to mark as done
    task_number = int(input("Enter task number to mark as done: ")) - 1
    # Update the status of the selected task to 'done'
    tasks[task_number]["done"] = True

# Main function to run the task management program
def main():
    # Main loop to continuously display the menu and process user input
    while True:
        # Display the menu options
        display_menu()
        # Prompt the user to enter their choice
        choice = input("Enter choice: ")
        # Based on the user's choice, call the corresponding function
        if choice == "1":
            add_task()  # Add a new task
        elif choice == "2":
            list_tasks()  # List all tasks
        elif choice == "3":
            mark_task_done()  # Mark a task as done
        elif choice == "4":
            break  # Exit the program if the user chooses to
        else:
            print("Invalid choice. Please choose again.")  # Inform the user of an invalid choice

# Entry point of the script
if __name__ == "__main__":
    main()
