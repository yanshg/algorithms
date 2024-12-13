'''
In Python, the threading module allows you to work with threads, and an Event is a synchronization primitive that allows one or more threads to wait for an event to occur. Here’s a simple example:
'''

import time
import threading

# Define a global variable
shared_resource = 0

# Create an event object
event = threading.Event()

# Define a function that waits for the event to be set
def wait_for_event(thread_id):
    print(f"Thread {thread_id} waiting for event to be set.")
    event.wait()  # Wait until the event is set
    print(f"Event is set. Thread {thread_id} proceeding.")
    global shared_resource
    shared_resource += 1
    print(f"Shared resource value: {shared_resource}")

# Define a function that sets the event
def set_event():
    print("Thread setting the event.")
    event.set()  # Set the event

# Create threads
threads = []
for i in range(3):
    t = threading.Thread(target=wait_for_event, args=(i,))
    threads.append(t)
    t.start()

# Simulate the event with some delay
time.sleep(2)

# Set the event
print("Event occurred! Notifying all threads...")
set_event()

# Wait for threads to complete
for t in threads:
    t.join()

print("All threads have completed execution.")