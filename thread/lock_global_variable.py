'''
Creating deadlock-free APIs that access the same variable involves careful management of concurrency. Here's an example using Python with threading and locks to ensure thread safety:

We use a lock to ensure that only one thread can access the shared variable at a time.
Each API function (api_1, api_2, api_3) acquires the lock before modifying the shared variable and releases it afterward.
This prevents deadlocks and ensures that the shared variable is updated safely.

'''

import threading

# Shared variable
shared_variable = 0
# Lock for synchronizing access to the shared variable
lock = threading.Lock()

def api_1():
    global shared_variable
    with lock:
        # Critical section
        shared_variable += 1
        print(f"API 1 incremented value to {shared_variable}")

def api_2():
    global shared_variable
    with lock:
        # Critical section
        shared_variable += 2
        print(f"API 2 incremented value to {shared_variable}")

def api_3():
    global shared_variable
    with lock:
        # Critical section
        shared_variable += 3
        print(f"API 3 incremented value to {shared_variable}")

# Creating threads for each API
thread1 = threading.Thread(target=api_1)
thread2 = threading.Thread(target=api_2)
thread3 = threading.Thread(target=api_3)

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Waiting for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print(f"Final value of shared variable: {shared_variable}")