import time
import threading

def task_1():
    time.sleep(10)
    print("Task 1 Completed")

def task_2():
    time.sleep(3)
    print("Task 2 Completed")

def task_3():
    time.sleep(5)
    print("Task 3 Completed")

# Calling functions on main thread
# task_1()
# task_2()
# task_3()

# Using Different Thread for the particular function
chore1 = threading.Thread(target=task_1)
chore1.start()

chore2 = threading.Thread(target=task_2)
chore2.start()

chore3 = threading.Thread(target=task_3)
chore3.start()
