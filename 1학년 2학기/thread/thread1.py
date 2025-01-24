import threading

def bar():
    for _ in range(5):
        print("hello")


    my_thread = threading.Thread(target = bar)

    my_thread.start()

    print("finish")
