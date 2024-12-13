'''
This is a classic case of an event notification mechanism in a multi-threaded environment. To handle this, you can use several approaches depending on the programming language and the synchronization primitives available. Here’s an overview of how this can be handled conceptually:
'''


import threading
import time

# Create a condition variable
condition = threading.Condition()

def thread_function(thread_id):
    print(f"Thread {thread_id} waiting for the event...")
    with condition:
        condition.wait()  # Wait until notified
        print(f"Thread {thread_id} received the event!")

# Create threads
threads = []
for i in range(3):
    t = threading.Thread(target=thread_function, args=(i,))
    threads.append(t)
    t.start()

# Simulate the event

time.sleep(2)  # Simulate some delay
print("Event occurred! Notifying all threads...")
with condition:
    condition.notify_all()  # Notify all waiting threads

# Wait for threads to complete
for t in threads:
    t.join()