todo_list=[]
name=input("Please enter your name\n")
prompt=f"Hello there,{name.title()}, what you want to do today\n1. Add task\n2. Remove task\n3. View task\n4. Exit CLI\n"
task=int(input(prompt))
while True:
    if task==1:
        new_task=input("Please enter the new task\n")
        todo_list.append(new_task)
        print(f"\nAdded to list,anything else {name.title()}?")
        task=int(input("1. Add task\n2. Remove task\n3. View task\n4. Exit CLI\n"))
    if task==2:
        removing=input("Please enter task to be removed")
        if removing in todo_list:
            todo_list.remove(removing)
            print("\nTask removed. Anything else?")
            task=int(input("1. Add task\n2. Remove task\n3. View task\n4.Exit CLI\n"))
        else:
            print(f"\nSorry,'{removing}' does not exist in task list. Please confirm task by viewing task list.")
            task=int(input("1. Add task\n2. Remove task\n3. View task\n4. Exit CLI\n"))
    if task==3:
        for all_tasks in todo_list:
            print(all_tasks.strip().capitalize())
            print("\nThese are all your tasks. Anything else?")
            task=int(input("1. Add task\n2. Remove task\n3. View task\n4. Exit CLI\n"))
    if todo_list==[]:
        print("\nList is empty")
        task=int(input("1. Add task\n2. Remove task\n3. View task\n4. Exit CLI\n"))
    if task==4:
        print("\nThanks for you for using the Chrys ToDo CLI app. Hope to see you soon(*-*)")
        break