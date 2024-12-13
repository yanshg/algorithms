'''
How to ensure that the register callback functions do not wait excessively to queue in the callback?

To ensure that the reg_cb method does not block excessively when queuing callbacks (especially in a multithreaded environment), we can implement the following measures:


Concurrent Processing with Worker Threads
If there are many callback requests and you don't want any to block, you can use a worker thread to handle queued callbacks asynchronously. This ensures that the main thread quickly queues requests without blocking.
'''

import time
import threading

from queue import Queue

POISON_PILL = None

class EventManager:
    def __init__(self):
        self.event_completed = False
        self.callback_queue = Queue()
        self.worker_thread = threading.Thread(target = self.process_queue, daemon = True)
        self.worker_thread.start()

    def reg_cb(self, callback):
        self.callback_queue.put(callback)

    def complete_event(self):
        self.event_completed = True

    def process_queue(self):
        while True:
            if self.event_completed:
                # Blocks until a callback is available
                callback = self.callback_queue.get()
                if callback is not POISON_PILL:
                    callback()

                # Formerly tell the queue that the task is completed
                self.callback_queue.task_done()
                
                if callback is POISON_PILL:
                    # If get POISON_PILL, end the thread
                    return
            else:
                # Do not block the CPU
                time.sleep(0.1)

    def close(self):
        # push poison pill to end the worker thread
        self.reg_cb(POISON_PILL)

        # Block until all items in the queue are processed
        self.worker_thread.join()
        self.callback_queue.join()

event_manager = EventManager()

def f1():
    print("Executing f1")
    time.sleep(5)
    print("finished execution for f1")

def f2():
    print("Executing f2")
    time.sleep(3)
    print("finished execution for f2")

def f3():
    print("Executing f3")
    time.sleep(3)
    print("finished execution for f3")

def user1():
    event_manager.reg_cb(f1)

def user2():
    event_manager.reg_cb(f2)

def user3():
    event_manager.reg_cb(f3)

print("start thr1")
thr1 = threading.Thread(target = user1)
thr1.start()

time.sleep(1)
print("start thr2")
thr2 = threading.Thread(target = user2)
thr2.start()

time.sleep(10)
event_manager.complete_event()

time.sleep(1)
print("start thr3")
thr3 = threading.Thread(target = user3)
thr3.start()

thr1.join()
thr2.join()
thr3.join()

print("start to close")
event_manager.close()
print("end")