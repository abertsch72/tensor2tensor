import pickle
import os


folder = "outputs/wiki_references/"
prefix = "process_"
def check():
    prior = pickle.load(open("completed.pkl", 'rb'))

    completed = []
    for proc in os.listdir(folder):
        complete = True
        files = os.listdir(folder + proc)
        if len(files) < 980:
            continue
        for file in files:
           if os.path.getsize(folder+proc+"/" + file) < 21:
               complete = False
               continue
        if complete:
           completed.append(int(proc.strip(prefix)))

    this_machine = completed
    print()
    print(this_machine)
    print(len(this_machine))


    completed.extend(prior)
    completed = sorted(list(set(completed)))
    with open("completed.pkl", "wb") as f:
        pickle.dump(completed, f)

    print(completed)
    print(len(completed))
 
    return completed


if __name__ == "__main__":
    check()
