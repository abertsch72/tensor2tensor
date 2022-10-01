
import os

from utils import shard
from check_completion import check 

all_wets = [u.strip().split("/")[-1] for u in open("outputs/wet.paths").readlines()]
completed = check() 

num_shards = 1000

assert len(all_wets) == 72000

sharded_wets = shard(all_wets, num_shards)

for i in completed:
    for file in sharded_wets[i]:
        potential_file = "outputs/wet_dir/" + file
        if os.path.exists(potential_file):
            print(f"removing {potential_file} from completed shard {i}")
            os.remove(potential_file)

