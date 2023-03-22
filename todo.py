def show_help():
    print("To-do list application")
    print("Commands:")
    print("  - HELP: Show this help message")
    print("  - ADD [task]: Add a new task")
    print("  - SHOW: Show all tasks")
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
		elif command == "EXIT":
			break
		else:
			print("Invalid command. Type 'HELP' for a list of commands.")


if __name__ == "__main__":
    main()
