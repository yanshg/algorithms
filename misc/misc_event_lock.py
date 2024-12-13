'''
Question: There are multiple users calling a method reg_cb at different instances of time, as shown below. Simultaneously, there is an event happening. All the user requests that were made during the execution of the event should wait till the event completes and then execute the reg_cb method. Once the event is finished, the user requests to the reg_cb method can be executed immediately. Implement how to handle the given scenario.


					Event in progress
----|---------------|--------------------|-------------------|--------------> timeline
U1: reg_cb(f1)     U2: reg_cb(f2)      Event completed      U3:reg_cb(f3)
									   (execute f1,f2)      (execute f3)
Was asked many questions on basic fundamentals like,



To handle the given scenario, you can use a thread-safe queue combined with a mechanism to ensure that all reg_cb requests wait until the event is completed. After the event finishes, the queued requests can be processed immediately, while subsequent requests execute without delay.


When does a concurrent modification exception occur?
When is the possibility of same thread (user x) calling the reg_cb() twice?
What are the possible deadlock scenarios?
What is mutex? etc..
Expectations: Concentrate on how you handle different possible scenarios with a valid scenario and explanation. Wrinting code is secondary.



'''

import threading
import time
import queue


class EventManager:
    def __init__(self):
        self.event_completed = False

        # Lock for synchronization
        self.event_lock = threading.Lock()

        # Thread-safe queue
        self.callback_queue = queue.Queue()

    def reg_cb(self, callback):
        # if event not completed, push callback into queue
        # queue need be thread-safe to support concurrence
        # if event completed, then call it immediately

        # 如果 callback 运行时间有点长，将导致 lock 比较长的时间
        with self.event_lock:
            if self.event_completed:
                print(f"{callback.__name__} is executing immediately")
                callback()
            else:
                # push cb into queue
                print(f"{callback.__name__} is waiting for the event complete")
                self.callback_queue.put(callback)
        
    def complete_event(self):
        # call the callbacks in queue one by one
        with self.event_lock:
            print(f"Event completed. Processing queued callbacks")
            self.event_completed = True
            while not self.callback_queue.empty():
                callback = self.callback_queue.get()
                callback()
                self.callback_queue.task_done()

    def close(self):
        self.callback_queue.join()

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

event_manager = EventManager()

def user1():
    event_manager.reg_cb(f1)

def user2():
    event_manager.reg_cb(f2)

def user3():
    event_manager.reg_cb(f3)



thr1 = threading.Thread(target=user1)
thr2 = threading.Thread(target=user2)

# push f1, f2 into queue
thr1.start()
time.sleep(1)
thr2.start()
time.sleep(1)

# set event complete and call callbacks in queue
event_manager.complete_event()

# 问题： 如果 callback 运行时间有点长，将导致 lock 比较长的时间， thr3 将被block住

time.sleep(1)

# call callback immediately after event complete
thr3 = threading.Thread(target=user3)
thr3.start()
print("thr3 started")

# wait for all threads to finish
thr1.join()
thr2.join()
thr3.join()

event_manager.close()
