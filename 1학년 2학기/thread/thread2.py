import threading

my_lock = threading.Lock()

def bar():
    for count in range(1,6):
        with my_lock:
            print(f"bar:{count}") # race condtion

def foo():
    for count in range(1,6):
        with my_lock:
            print(f"foo:{count}") # race condtion

thread_1 = threading.Thread(target = bar)
thread_2 = threading.Thread(target = foo)


thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()


print("finish") 