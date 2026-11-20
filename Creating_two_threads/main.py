import threading

s = threading.Semaphore(1) # if we put 0 - program will run without stop bcs we have 2 acquires

def first():
    s.acquire()
    print("First thread is running")
    s.release()

def second():
    s.acquire()
    print("Second thread is running")
    s.release()

t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)

t1.start()
t2.start()

t1.join()
t2.join()