import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing

def integrate(f, a, b, n_iter, left, right):
    acc = 0
    step = (b - a) / n_iter
    for i in range(left, right):
        acc += f(a + i * step) * step
    return acc

def thread_integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    sz = n_iter // n_jobs

    threads = []

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            left = i * sz
            if i == n_jobs - 1:
                right = n_iter
            else:
                right = (i + 1) * sz
            future = executor.submit(integrate, f, a, b, n_iter, left, right)
            threads.append(future)
    res = 0
    for future in threads:
        res += future.result()
    return res


def process_integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    sz = n_iter // n_jobs

    processes = []

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            left = i * sz
            if i == n_jobs - 1:
                right = n_iter
            else:
                right = (i + 1) * sz
            future = executor.submit(integrate, f, a, b, n_iter, left, right)
            processes.append(future)
    res = 0
    for future in processes:
        res += future.result()
    return res

if __name__ == '__main__':
    cpu_num = multiprocessing.cpu_count()

    thread_time = 0
    process_time = 0

    
    with open("integrate.txt", "w") as file:
        file.write("n_jobs ThreadPool ProcessPool\n")
        for n_jobs in range(1, cpu_num * 2 + 1):
            x = time.time()
            res = thread_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
            y = time.time()

            time1 = y - x

            x = time.time()
            res = process_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
            y = time.time()
            time2 = y - x

            file.write(str(n_jobs) + " " + str(time1) + " " + str(time2) + "\n")

