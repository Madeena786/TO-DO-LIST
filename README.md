# **Build a Simple To-Do List**



## **Task 8 – Python Programming Track**





###### **Project Description**

This project is a simple command-line To-Do List application developed using Python.

The application allows users to add, view, update, and remove tasks through a menu-driven interface.

The project helps to understand Python lists, loops, conditions, functions, and CRUD operations.



###### **Objective**

The main objective of this project is to learn:



1. Python Lists
2. Functions
3. Loops
4. Conditional Statements
5. User Input
6. Menu-Driven Programs
7. CRUD Operations



###### **Technologies Used**



Python



###### **Features**



The To-Do List application provides the following features:



1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit the Application



###### **CRUD Operations**

CRUD stands for:



* Create – Add a new task
* Read – View existing tasks
* Update – Modify an existing task
* Delete – Remove a task



###### **How the Program Works**

The program stores tasks in a Python list.



When the program starts, it displays a menu:



1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit



The user selects an option by entering the corresponding number.

**Add Task:**

The user enters a task, and the task is added to the list using the `append()` method.



**View Tasks:**

The program displays all the tasks stored in the list with their task numbers.



**Update Task:**

The user enters the task number and provides a new task. The selected task is replaced with the new task.



**Remove Task:**

The user enters the task number, and the selected task is removed from the list using the `pop()` method.



**Exit**:

The program stops when the user selects the Exit option.



###### **Python Program**



tasks = \[]

def addtask():

&#x20;   t=input("Enter a task: ")

&#x20;   tasks.append(t)

&#x20;   print("Task added successfully!")

def viewtasks():

&#x20;   if len(tasks)== 0:

&#x20;       print("No tasks available.")

&#x20;   else:

&#x20;       print("\\nYour Tasks:")

&#x20;       for i in range(len(tasks)):

&#x20;           print(i + 1, ".", tasks\[i])

def updatetask():

&#x20;   viewtasks()

&#x20;   if len(tasks) == 0:

&#x20;       return

&#x20;   n=int(input("Enter task number to update: "))

&#x20;   if n>=1 and n<=len(tasks):

&#x20;       newtask=input("Enter new task: ")

&#x20;       tasks\[n-1]=newtask

&#x20;       print("Task updated successfully!")

&#x20;   else:

&#x20;       print("Invalid task number.")

def removetask():

&#x20;   viewtasks()

&#x20;   if len(tasks)==0:

&#x20;       return

&#x20;   n=int(input("Enter task number to remove: "))

&#x20;   if n>=1 and n<=len(tasks):

&#x20;       tasks.pop(n-1)

&#x20;       print("Task removed successfully!")

&#x20;   else:

&#x20;       print("Invalid task number.")

while True:

&#x20;   print("\\n\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*")

&#x20;   print("1. Add Task")

&#x20;   print("2. View Tasks")

&#x20;   print("3. Update Task")

&#x20;   print("4. Remove Task")

&#x20;   print("5. Exit")

&#x20;   c=input("Enter your choice:")

&#x20;   if c=="1":

&#x20;       addtask()

&#x20;   elif c=="2":

&#x20;       viewtasks()

&#x20;   elif c=="3":

&#x20;       updatetask()

&#x20;   elif c=="4":

&#x20;       removetask()

&#x20;   elif c=="5":

&#x20;       print("Thank you for using To-Do List!")

&#x20;       break

&#x20;   else:

&#x20;       print("Invalid choice. Please try again.")



###### **Sample Execution**



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:1

Enter a task: Reading A book

Task added successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:1

Enter a task: writing a notes

Task added successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:1

Enter a task: ckleaning dishes

Task added successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:1

Enter a task: washing clothes

Task added successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:3



Your Tasks:

1 . Reading A book

2 . writing a notes

3 . ckleaning dishes

4 . washing clothes

Enter task number to update: 1

Enter new task: reading a book

Task updated successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:3



Your Tasks:

1 . reading a book

2 . writing a notes

3 . ckleaning dishes

4 . washing clothes

Enter task number to update: 3

Enter new task: cleaning dishes

Task updated successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:1

Enter a task: sleeping

Task added successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:4



Your Tasks:

1 . reading a book

2 . writing a notes

3 . cleaning dishes

4 . washing clothes

5 . sleeping

Enter task number to remove: 5

Task removed successfully!



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:2



Your Tasks:

1 . reading a book

2 . writing a notes

3 . cleaning dishes

4 . washing clothes



\*\*\*\*\*\*\*\*\*\*\*TO-DO LIST\*\*\*\*\*\*\*\*\*\*\*

1\. Add Task

2\. View Tasks

3\. Update Task

4\. Remove Task

5\. Exit

Enter your choice:5

Thank you for using To-Do List!



###### **Concepts Used**



* Lists
* Functions
* input()
* print()
* if-elif-else
* while loop
* for loop
* append()
* pop()
* len()
* break
* CRUD Operations



###### **Conclusion:**

The Simple To-Do List project demonstrates how Python can be used to create a basic command-line application.

This project helped me understand lists, functions, loops, conditions, user input, and CRUD operations in Python.



