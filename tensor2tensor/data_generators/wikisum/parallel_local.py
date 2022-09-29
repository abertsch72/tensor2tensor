

"""
flags:

flags.DEFINE_integer("num_tasks", 1, "Number of parallel tasks.")
flags.DEFINE_integer("task_id", 0, "Task id in a parallel run.")

"""
import time
import sys
import random
start = int(sys.argv[1])
end = int(sys.argv[2])
num_tasks = 1000

command = "python3 get_references_commoncrawl.py --task_id "
from multiprocessing import Process, Lock, Pool, cpu_count


from timeit import default_timer as timer

from get_references_commoncrawl import call

def f(i, outdir="outputs/wiki_references"):
    sleeptime = random.randint(0,20) # stagger downloads 
    time.sleep(sleeptime)
    try:
        call(i, outdir)
    except:
        print("error in process " + str(i))
        time.sleep(100)
        print("NOTE: retrying " + str(i))
        f(i, outdir)

    
if __name__ == '__main__':

    proc = []
    indices = list(range(start, end))
    start = timer()

    print(f'starting computations on {cpu_count()} cores')

    with Pool() as pool:
        pool.map(f, indices)
    end = timer()
    print(f'elapsed time: {end - start}')

    """
    for num in range(start,end):
        p = Process(target=f, args=(num,))
        p.start()
        p.join()
        proc.append(p)
        if num % 5 == 0:
            time.sleep(20) 
    """
