import threading,time

def thread_func(name):
    print("Starting thread ", name)
    time.sleep(2)
    print("Finishing thread ", name)

if __name__ == '__main__':
    print("Main: creating the threads")
    threads = [ threading.Thread(target=thread_func, args=(i,), daemon=True) for i in range(10) ]

    print("Main: starting the threads")
    for t in threads:
        t.start()

    print("Main: waiting the threads end")
    for t in threads:
        t.join()


