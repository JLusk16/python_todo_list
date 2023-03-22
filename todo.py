def show_help():
    print("To-do list application")
    print("Commands:")
    print("  - HELP: Show this help message")
    print("  - ADD [task]: Add a new task")
    print("  - SHOW: Show all tasks")
    print("  - REMOVE [task_number]: Remove a task by its number")
    print("  - EXIT: Exit the application")

def add_task(task,tasks):
	tasks.append(task)
	print(f"Added task: {task}")

def show_tasks(tasks):
	if not tasks:
		print("No tasks in the list")
	else:
		for index, task in enumerate(tasks, start=1):
			print(f"{index}. {task}")

def remove_task(task_list, task_number):
    try:
        index = int(task_number) - 1
        if 0 <= index < len(task_list):
            removed_task = task_list.pop(index)
            print(f"Removed task: {removed_task}")
        else:
            print(f"Invalid task number: {task_number}")
    except ValueError:
        print("Please enter a valid task number to remove")

def main():
	tasks = []
	while True:
		command = input("> ").upper()
		if command == "HELP":
			show_help()
		elif command.startswith("ADD"):
			task = command[4:].strip()
			add_task(task,tasks)
		elif command == ("SHOW"):
			show_tasks(tasks)
		elif command == "REMOVE":
			if len(command_parts) > 1:
				remove_task(task_list, command_parts[1])
		elif command == "EXIT":
			break
		else:
			print("Invalid command. Type 'HELP' for a list of commands.")


if __name__ == "__main__":
    main()
