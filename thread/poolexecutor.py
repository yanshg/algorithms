import threading,time
import concurrent.futures

def thread_func(name):
    print("starting thread ", name)
    time.sleep(2)
    print("finishing thread ", name)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            executor.submit(thread_func, i)
