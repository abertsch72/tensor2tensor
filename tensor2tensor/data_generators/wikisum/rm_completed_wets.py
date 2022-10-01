
import os

from utils import shard
from check_completion import check 

all_wets = [u.strip().split("/")[-1] for u in open("outputs/wet.paths").readlines()]
completed = check() # [662, 652, 663, 9, 941, 4, 984, 16, 901, 907, 981, 1, 853, 980, 902, 22, 945, 857, 855, 15, 13, 854, 19, 906, 21, 17, 904, 900, 942, 986, 944, 946, 14, 905, 2, 943, 3, 940, 982, 985, 20, 11, 0, 983, 947, 12, 18, 6, 850, 903, 987, 5, 851]
num_shards = 1000

assert len(all_wets) == 72000

sharded_wets = shard(all_wets, num_shards)

for i in completed:
    for file in sharded_wets[i]:
        potential_file = "outputs/wet_dir/" + file
        if os.path.exists(potential_file):
            print(f"removing {potential_file} from completed shard {i}")
            os.remove(potential_file)

