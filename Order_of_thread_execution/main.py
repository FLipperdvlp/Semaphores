import threading

s = threading.Semaphore(0)

def first():
    print("first thread")
    s.release()

def second():
    s.acquire()
    print("second thread")
    s.release()

t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)

t2.start()
t1.start()

t1.join()
t2.join()