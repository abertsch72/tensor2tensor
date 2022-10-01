import os

completed = [662, 652, 663, 9, 941, 4, 984, 16, 901, 907, 981, 1, 853, 980, 902, 22, 945, 857, 855, 15, 13, 854, 19, 906, 21, 17, 904, 900, 942, 986, 944, 946, 14, 905, 2, 943, 3, 940, 982, 985, 20, 11, 0, 983, 947, 12, 18, 6, 850, 903, 987, 5, 851]
wets_downloaded = "outputs/wet_dir"

from utils import shard

all_wets = [u.strip() for u in open("outputs/wet.paths").readlines()]
completed = [662, 652, 663, 9, 941, 4, 984, 16, 901, 907, 981, 1, 853, 980, 902, 22, 945, 857, 855, 15, 13, 854, 19, 906, 21, 17, 904, 900, 942, 986, 944, 946, 14, 905, 2, 943, 3, 940, 982, 985, 20, 11, 0, 983, 947, 12, 18, 6, 850, 903, 987, 5, 851]
num_shards = 1000

assert len(all_wets) == 72000

sharded_wets = shard(all_wets, num_shards)

wets = os.listdir("outputs/wet_dir")
wets = [wet for wet in wets if os.path.getsize(wets_downloaded + "/" + wet) > 1000]

represented = {}
for j, url in enumerate(wets):
    for i, shard in enumerate(sharded_wets):
        shard = [s.split("/")[-1] for s in shard]
        if url in shard:
            if i in completed:
                print(f"completed {url} from shard {i}")
            else:
                represented[i] = represented.get(i,0) + 1
            continue

complete = []
fill_partial = []
for shard in represented:
    if represented[shard] == 72:
        complete.append(shard)
    else:
        fill_partial.extend([url for url in sharded_wets[shard] if url not in wets])

print(represented)
print(complete)
for f in fill_partial:
    print(f)
