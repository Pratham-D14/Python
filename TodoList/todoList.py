todos = {}

def addTodo(id: int, todo: str):
    todos[id] = todo
    print("updated todo: ", todos)


def removeTodo(id):
    del todos[id]
    print("updated todo: ", todos)


def readTodos():
    print(todos)


while True:
    try:
        operation = input("What functionality you have to do (Add/Delete/Read): ")
        if operation == "Read":
            readTodos()
        elif operation == 'Add':
            todoId: int = int(input("Enter Todo ID: "))
            todoDesc: str = str(input("Enter Todo Description: "))
            addTodo(todoId, todoDesc)
        elif operation == "Delete":
            todoId: int = int(input("Enter Todo ID: "))
            removeTodo(todoId)
        else:
            print("Please enter valid Functionality (Add / Delete / Read)")

        doMore = input("Do you want to continue (y/n): ")
        if doMore != "y":
            break
        continue
    except ValueError:
        print("Please Enter valid values")


