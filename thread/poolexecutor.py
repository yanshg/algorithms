import threading,time
import concurrent.futures

global_variable = 0
lock = threading.Lock()

def thread_func(i):
    print("starting thread ", i, "global_variable: ", global_variable)
    time.sleep(5)
    with lock:
        global_variable += i

    print("finishing thread ", i, "global_variable: ", global_variable)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(10):
            executor.submit(thread_func, i)
