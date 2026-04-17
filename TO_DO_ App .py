todo_list = []


def view_tasks():
    print("\nYour To Do List:")
    if len(todo_list) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task} ")
        print("\n")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "status": "pending"})
    print(f"Task '{task}' added successfully.")

def delete_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            view_tasks()
            task_index = int(input("Enter the task number to delete: ")) -1
            if 0 <= task_index < len(todo_list):
                deleted_task = todo_list.pop(task_index)
                print(f"Task '{deleted_task['task']}' deleted successfully.")
            else:
                print("Invalid task number.")
        
        except ValueError:
            print("Please enter a valid task number.")
        
def mark_task_completed():     
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            view_tasks()
            task_index = int(input("Enter the task number to mark as Complete: ")) -1
            if 0 <= task_index < len(todo_list):
                todo_list[task_index]['status'] = 'completed'
                print(f"Task '{todo_list[task_index]['task']}' marked as completed.")
        except ValueError:
            print("Please enter a valid task number.")

def exit_app():
    print("Exiting the application.")
    exit()


def todo_list_app():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View AllTasks")
        print("2. Add a New Task")
        print("3. Mark a Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            view_tasks()

        elif choice == '2':
            add_task()

        elif choice == '3':
            mark_task_completed()

        elif choice == '4':
            delete_task()

        elif choice == '5':
            exit_app()
        else:
            print("Invalid choice. Please try again.")



todo_list_app()