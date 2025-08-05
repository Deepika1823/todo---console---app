def load_tasks():
    try:
        with open("tasks.txt","r")as file:
            return[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
         for task in tasks:
            file.write(task + "\n")


def task():
    tasks = load_tasks() 
    print("........WELCOME TO THE TASK MANAGEMENT APP........")
    try:
        total_task = int(input("Enter how many tasks you want to add = "))
        for i in range(1, total_task+1):
            task_name = input(f"Enter task {i} = ")
            tasks.append(task_name)
        save_tasks(tasks)
        print(f"Today`s tasks are\n({tasks}")
    except ValueError:
        print("Please enter a valid number.")

    while True:
        try:

            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        except ValueError:
            print("Invalid input.Please enter a value between 1 and 5 ")
            continue        
        if operation== 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            save_tasks(tasks)
            print(f"Task {add} has been sucessfully added...")

        elif operation == 2:
            updated_val = input("Enter the task you wanted to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
        elif operation == 3:
            del_val = input("Which task you want to delete =")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        elif operation == 4:
            print(f"Total tasks = {tasks}")
        elif operation == 5:
            print(f"Closing the program.....")
            break
        else:
            print("Invalid Input")        


task()                
