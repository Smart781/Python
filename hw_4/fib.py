import time
from threading import Thread
from multiprocessing import Process

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


def SynchFib(n):
    a = time.time()
    for i in range(10):
        Fib(n)      
    b = time.time()

    return b - a


def ThreadFib(n):
    a = time.time()
    threads = []
    for i in range(10):
        t = Thread(target=Fib, args=(n, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    b = time.time()

    return b - a

def ProcessFib(n):
    a = time.time()
    processes = []
    for i in range(10):
        p = Process(target=Fib, args=(n, ))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    b = time.time()

    return b - a

if __name__ == '__main__':
    n = 30
    res1 = SynchFib(n)
    res2 = ThreadFib(n)
    res3 = ProcessFib(n)
    
    with open("fib.txt", "w") as file:
        file.write("synch: " + str(res1) + "\n")
        file.write("threading: " + str(res2) + "\n")
        file.write("multiprocessing: " + str(res3) + "\n")
    
