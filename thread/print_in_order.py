import threading,time

class Solution:
    def __init__(self):
        self.first_lock=threading.Lock()
        self.second_lock=threading.Lock()
        self.third_lock=threading.Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()
        self.third_lock.acquire()

    def print_first(self):
        print("starting first sub")
        time.sleep(1.1)
        print("first")
        time.sleep(1)
        self.second_lock.release()

    def print_second(self):
        with self.second_lock:
            print("starting second sub")
            time.sleep(1)
            print("second")
            time.sleep(1)
            self.third_lock.release()

    def print_third(self):
        with self.second_lock:
            print("starting third sub")
            time.sleep(1)
            print("third")
            time.sleep(1)


solution=Solution()

t1=threading.Thread(target=solution.print_first, daemon=True)
t2=threading.Thread(target=solution.print_second, daemon=True)
t3=threading.Thread(target=solution.print_third, daemon=True)

threads=[t1, t2, t3]

for t in threads:
    t.start()

for t in threads:
    t.join()
