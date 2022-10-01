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
# comp2: [9, 941, 4, 984, 16, 901, 907, 981, 1, 853, 980, 902, 22, 945, 857, 855, 15, 13, 854, 19, 906, 21, 17, 904, 900, 942, 986, 944, 946, 14, 905, 2, 943, 3, 940, 982, 985, 20, 11, 0, 983, 947, 12, 18, 6, 850, 903, 987, 5, 851]

