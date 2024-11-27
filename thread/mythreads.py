import threading, time

global_variable = 0
lock = threading.Lock()

def thread_func(i):
    global global_variable

    print(f"Starting thread {i}, global_variable: {global_variable}")
    time.sleep(1)
    with lock:
        global_variable += i

    print(f"Finishing thread {i}, global_variable: {global_variable}")

if __name__ == '__main__':
    print("Main: creating the threads")
    threads = [ threading.Thread(target=thread_func, args=(i,), daemon=True) for i in range(10) ]

    print("Main: starting the threads")
    for t in threads:
        t.start()

    print("Main: waiting the threads end")
    for t in threads:
        t.join()


