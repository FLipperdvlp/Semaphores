from threading import Semaphore, Thread

a = Semaphore(1)
b = Semaphore(0)
c = Semaphore(0)

def first():
    for _ in range(5):
        a.acquire()
        print("A", end="")
        b.release()
def second():
    for _ in range(5):
        b.acquire()
        print("B", end="")
        c.release()
def third():
    for _ in range(5):
        c.acquire()
        print("C", end="")
        a.release()

t1 = Thread(target=first)
t2 = Thread(target=second)
t3 = Thread(target=third)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()