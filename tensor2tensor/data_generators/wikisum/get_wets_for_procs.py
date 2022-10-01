import os
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

from utils import shard

all_wets = [u.strip() for u in open("outputs/wet.paths").readlines()]

completed = [0, 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 171, 310, 313, 324, 332, 340, 342, 356, 357, 449, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 467, 468, 469, 472, 473, 474, 475, 476, 484, 586, 604, 609, 615, 628, 652, 662, 663, 736, 738, 746, 750, 753, 761, 777, 850, 851, 853, 854, 855, 857, 867, 872, 887, 900, 901, 902, 903, 904, 905, 906, 907, 940, 941, 942, 943, 944, 945, 946, 947, 980, 981, 982, 983, 984, 985, 986, 987, 991]
desired = [i for i in range(start,end) if i not in completed]
num_shards = 1000

assert len(all_wets) == 72000

sharded_wets = shard(all_wets, num_shards)


represented = {}
for i in desired:
    shard = sharded_wets[i]
    for url in shard:
         print(url)
