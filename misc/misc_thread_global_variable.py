'''

threads in Python share the same memory space as the main program, which means they have access to global variables.

Important Considerations:

Race Conditions:
If multiple threads try to modify a global variable at the same time, you can encounter race conditions, leading to unpredictable results.

Synchronization:
To avoid race conditions, you can use synchronization mechanisms like locks, semaphores, or condition variables.

Thread-Local Storage:
If you need variables that are unique to each thread, you can use the threading.local() class.

'''

import threading

lock = threading.Lock()
global_variable = 0

def increment_global(thread_id):
    with lock:
        print(f"Executing thread {thread_id}")
        global global_variable
        for _ in range(100000):
            global_variable += 1

threads = []
for i in range(6):
    thread = threading.Thread(target=increment_global, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Final value:", global_variable)
