import os


completed = []

folder = "outputs/wiki_references/"
prefix = "process_"

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
        print(proc.strip(prefix))

print(completed)


# comp1: [662, 652, 663]

