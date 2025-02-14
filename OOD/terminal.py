class Task():
    def __init__(self, name):
        self.name = name
        self.status = False
    def mark_done(self):
        self.status = True
    def __str__(self):
        return self.name
class TaskManager():
    def __init__(self):
        self.tasks = []
    def add_task(self, task_name: str):
        new_task = Task(task_name)
        self.tasks.append(new_task)
        return new_task
    def remove_task(self, task_id:int):
        if 0 <= task_id < len(self.tasks):
            removed = self.tasks.pop(task_id)
            return removed
        else:
            raise("No task with id:", task_id)
    def list_tasks(self):
        return self.tasks
    def mark_task_done(self, index:int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            return self.tasks[index]
        else:
            raise IndexError("Invalid task index")
class CLI():
    def __init__(self, task_manager:TaskManager):
        self.task_manager = task_manager
        self.commands = {
            "help": self.show_help,
            "add": self.add_task_command,
            "list": self.list_tasks_command,
            "remove": self.remove_task_command,
            "done": self.done_task_command,
            "exit": self.exit_command
        }
    def show_help(self, args):
        print("Available commands:")
        print("  help                Show this help message")
        print("  add <title>         Add a new task")
        print("  list                List all tasks")
        print("  remove <index>      Remove a task by its index")
        print("  done <index>        Mark a task as done by its index")
        print("  exit                Exit the program")
    def add_task_command(self, args):
        if args is None:
            print("Usage: add <title of the task>")
            return
        task_name = " ".join(args)
        task = self.task_manager.add_task(task_name)
        print(f"Added task: {task}") 
    def list_tasks_command(self, args):
        tasks = self.task_manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}. {task}")
    def remove_task_command(self, args):
        if not args:
            print("Usage: remove <index>")
            return
        try:
            index = int(args[0])
            removed_task = self.task_manager.remove_task(index)
            print(f"Removed task: {removed_task}")
        except ValueError:
            print("Error: Index must be an integer.")
    def done_task_command(self, args):
        if not args:
            print("Usage: done <index>")
            return
        try:
            index = int(args[0])
            done_task = self.task_manager.mark_task_done(index)
            print(f"Task {done_task} is done")
        except ValueError:
            print("Error: Index must be an integer.")
    def exit_command(self, args):
        print("Exiting the program. Goodbye!")
        exit(0)
    def run(self):
        while True:
            user_input = input("> ").strip()
            if not user_input:
                continue
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]
            if command in self.commands:
                try:
                    self.commands[command](args)
                except IndexError as e:
                    print(f"Error: {e}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Unknown command: '{command}'. Type 'help' for instructions.")
task_manager = TaskManager()
cli = CLI(task_manager)
cli.run()