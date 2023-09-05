# a simple to-do list application that can be run in the Python Terminal. This program allows you to add tasks, view your to-do list, mark tasks as completed, and remove tasks.

class Todo_List:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        if self.tasks:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("\nThere are no tasks in your To-Do List!")
    
    def completed_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            task_done = self.tasks.pop(task_num - 1)
            print(f"Task {task_done} has been marked as completed")
        else:
            print("Invalid Task Number!")

    def remove_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            task_removed = self.tasks.pop(task_num - 1)
            print(f"Task {task_removed} has been removed!")
        else:
            print("Invalid Task Number!")
        
       
def main():
    run = True
    todo_list = Todo_List()
    
    
    while run:
        print("\n--------------------------")
        print("Here are the options:")
        print("1. Add a Task")
        print("2. View your Tasks")
        print("3. Mark a Task as Complete")
        print("4. Remove a Task")
        print("5. Quit")
        print("--------------------------")
        
        choice = int(input("\nChoose a Number please: "))
        
        match choice:
            case 1:
                task = input("Write down a task you want to add: ")
                todo_list.add_task(task)
                print("Task has been successfully added!")
            case 2: todo_list.view_tasks()
            case 3:
                if len(todo_list.tasks) > 0: 
                    todo_list.view_tasks()
                    num = int(input("\nPlease give us the number of the task you want to mark as complete: "))
                    todo_list.completed_task(num)
                else: 
                    print("\nThere are no tasks in your To-Do List!")
            case 4:
                if len(todo_list.tasks) > 0:
                    todo_list.view_tasks()
                    num = int(input("\nPlease give us the number of the task you want to remove: "))
                    todo_list.remove_task(num)
                else: 
                    print("\nThere are no tasks in your To-Do List!")
            case 5:
                print("Thank you for using the To-Do List!")
                break
            case _: print("Task Number does not exist!")


if __name__ == "__main__":
    print("\nSimple To-Do List\n")
    main()


