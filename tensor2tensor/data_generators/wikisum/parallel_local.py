

"""
flags:

flags.DEFINE_integer("num_tasks", 1, "Number of parallel tasks.")
flags.DEFINE_integer("task_id", 0, "Task id in a parallel run.")

"""

num_tasks = 40

command = "python3 get_references_commoncrawl.py --task_id "
indices = list(range(0, num_tasks))
from multiprocessing import Process, Lock
from get_references_commoncrawl import call

def f(i, outdir):
    call(i, outdir)

if __name__ == '__main__':

    for num in range(2):
        Process(target=f, args=(num,"outputs/wiki_references")).start()