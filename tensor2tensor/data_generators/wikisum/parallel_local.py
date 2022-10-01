

"""
flags:

flags.DEFINE_integer("num_tasks", 1, "Number of parallel tasks.")
flags.DEFINE_integer("task_id", 0, "Task id in a parallel run.")

"""
import time
import sys
import random
#start = int(sys.argv[1])
#end = int(sys.argv[2])
num_tasks = 1000

command = "python3 get_references_commoncrawl.py --task_id "
from multiprocessing import Process, Lock, Pool, cpu_count, get_context


from timeit import default_timer as timer

from get_references_commoncrawl import call

def f(i, outdir="outputs/wiki_references"):
    sleeptime = random.randint(1000000,20000000) # stagger downloads 
    s = 0
    for j in range(sleeptime):
        s += j
        s -= j
    try:
        call(i, outdir)
    except EOFError as e:
        print(e)
        print("FILE error in process " + str(i))
        #print("NOTE: retrying " + str(i))
        #f(i, outdir)

    
if __name__ == '__main__':

    proc = []

    indices = list(range(25,50))

    start_time = timer()

    print(f'starting computations on {cpu_count()} cores')

    with get_context("spawn").Pool(int(cpu_count() / 2)) as pool:
        pool.map(f, indices)

    """
    for num in range(start,end):
        p = Process(target=f, args=(num,))
        p.start()
        #p.join()
        proc.append(p)
    print(len(proc))
    end_time = timer()
    print(f'elapsed time: {end - start}')
    """

def distribute(indices, half=True):
    print(f'starting computations on {cpu_count()} cores')
    poolsize = cpu_count()
    if half:
        poolsize = int(poolsize / 2)
    start_time = timer()
    with get_context("spawn").Pool(poolsize) as pool:
        pool.map(f, indices)
    end_time = timer()
    print(f'elapsed time: {end - start}')

