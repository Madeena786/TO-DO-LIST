tasks = []
def addtask():
    t=input("Enter a task: ")
    tasks.append(t)
    print("Task added successfully!")
def viewtasks():
    if len(tasks)== 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
def updatetask():
    viewtasks()
    if len(tasks) == 0:
        return
    n=int(input("Enter task number to update: "))
    if n>=1 and n<=len(tasks):
        newtask=input("Enter new task: ")
        tasks[n-1]=newtask
        print("Task updated successfully!")
    else:
        print("Invalid task number.")
def removetask():
    viewtasks()
    if len(tasks)==0:
        return
    n=int(input("Enter task number to remove: "))
    if n>=1 and n<=len(tasks):
        tasks.pop(n-1)
        print("Task removed successfully!")
    else:
        print("Invalid task number.")
while True:
    print("\n***********TO-DO LIST***********")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")
    c=input("Enter your choice:")
    if c=="1":
        addtask()
    elif c=="2":
        viewtasks()
    elif c=="3":
        updatetask()
    elif c=="4":
        removetask()
    elif c=="5":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice. Please try again.")

        
