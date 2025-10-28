import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{i+1}. {task['title']} - {status}")
    print()

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to mark as done: ")) - 1
        tasks[choice]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as done!\n")
    except (ValueError, IndexError):
        print("❌ Invalid choice.\n")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        deleted = tasks.pop(choice)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {deleted['title']}\n")
    except (ValueError, IndexError):
        print("❌ Invalid choice.\n")

def main():
    tasks = load_tasks()

    while True:
        print("=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.\n")

if __name__ == "__main__":
    main()
