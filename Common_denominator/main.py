import threading

counter = 0
s = threading.Semaphore(1)

def increase():
    global counter

    for i in range(1000):
        s.acquire()
        counter += 1
        s.release()


t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)