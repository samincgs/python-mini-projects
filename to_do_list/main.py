# a simple to-do list application that can be run in the Python Terminal. This program allows you to add tasks, view your to-do list, mark tasks as completed, and remove tasks:

class Todo_List:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("There are no tasks in your To-Do List!")
    
    def completed_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            task_done = self.tasks.pop(task_num)
            print(f"Task {task_done} has been marked as completed")
        else:
            print("Task Number does not exist!")

    def remove_task(self, task_num):
        if 1<= task_num <= len(self.tasks):
            task_removed = self.tasks.pop(task_num)
            print(f"Task {task_removed} has been removed!")
        else:
            print("Task Number does not exist!")

def main():
    run = True
    todo_list = Todo_List()
    
    
    while run:
        print("Here are the options:\n")
        print("1. Add a Task")
        print("2. View your Tasks")
        print("3. Mark a Task as Complete")
        print("4. Remove a Task")
        print("5. Quit")
        
        choice = input("Choose a Number please")
        return run



if __name__ == "__main__":
    print("\nSimple To-Do List\n")
    main()


