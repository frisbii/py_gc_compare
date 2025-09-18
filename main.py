import time
import sys

def baseline():
    x = 0
    for i in range(100000):
        x += i
    return x

def main():
    times = []
    for i in range(100):
        t0 = time.time()
        baseline()
        t1 = time.time()
        times.append(t1 - t0)
    avg = sum(times) / len(times)
    print("avg: %.10f" % avg)

main()