import time
import os
import sys
import csv

TIMESTAMP = ""
INTERPRETER = ""
time_base = 0

def baseline():
    x = 0
    for i in range(100000):
        x += i
    return x

def mac():
    x = 0
    for i in range(100000):
        x += i*i
    return x

def short_lives():
    for i in range(100000):
        x = [0,1,2,3]
    return 0

def short_cycles():
    for i in range(100000):
        a, b = {}, {}
        a["fiz"] = b
        b["baz"] = a
    return 0

def write_result(benchmark, result, speedup=1.0):
    outpath = "./results/%s.csv" % TIMESTAMP
    with open(outpath, "a") as f:
        writer = csv.writer(f, lineterminator="\n")
        if not os.path.getsize(outpath):
            writer.writerow(["interpreter", "benchmark", "result", "speedup"])
        writer.writerow([INTERPRETER, benchmark, result, speedup])

def run(benchmark):
    global time_base
    times = []
    for i in range(100):
        t0 = time.time()
        benchmark()
        t1 = time.time()
        times.append(t1 - t0)
    bench_name = benchmark.__name__
    avg = sum(times) / len(times)
    speedup = 1.0

    if bench_name == "baseline":
        print("\t" + ("%s avg: " % bench_name).ljust(20) + "%.10f" % avg)
        time_base = avg
    else:
        speedup = time_base / avg
        print("\t" + ("%s avg: " % bench_name).ljust(20) + "%.10f" % avg + "\t\tspeedup: %.3fx" % speedup)
    
    write_result(bench_name, avg, speedup)



if __name__ == "__main__":

    TIMESTAMP = sys.argv[1]
    INTERPRETER = sys.argv[2]

    tests = [baseline, mac, short_lives, short_cycles]
    for test in tests:
        run(test)