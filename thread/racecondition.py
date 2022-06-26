import threading,time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.val = 0

    def update(self,name):
        print("starting thread ", name)
        local_copy = self.val
        local_copy += 1
        time.sleep(2)
        self.val = local_copy
        print("finishing thread ", name)

if __name__ == '__main__':
    db = FakeDatabase()
    db.update(1)
    print("Main thread, start db value: {}".format(db.val))
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            executor.submit(db.update, i)
    print("Main thread, end db value: {}".format(db.val))

