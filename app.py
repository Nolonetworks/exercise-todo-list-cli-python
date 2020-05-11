import csv
todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    todos.append(title)
    print(todos)
    return todos
    pass

def print_list():
    global todos
    for item in todos:
        print(item)
    pass

def delete_task(number_to_delete):
    # your code here
    number_to_delete = int(number_to_delete) - 1
    todos.pop(number_to_delete)
    return todos
    pass

def save_todos():
    # your code here
    global todos
    tareas = ""
    i=0
    for item in todos:
        
        if i == 0:
            tareas = tareas + item
            i = i + 1
        else:
            tareas = tareas + "," + item
        print(tareas)

    archivo  = open("tareas.csv","w+")
    archivo.write(tareas)
    archivo.close()
    pass

    
def load_todos():
    # your code here
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")