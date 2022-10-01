import os

completed = [662, 652, 663, 9, 941, 4, 984, 16, 901, 907, 981, 1, 853, 980, 902, 22, 945, 857, 855, 15, 13, 854, 19, 906, 21, 17, 904, 900, 942, 986, 944, 946, 14, 905, 2, 943, 3, 940, 982, 985, 20, 11, 0, 983, 947, 12, 18, 6, 850, 903, 987, 5, 851]
all_wets = "outputs/wet.paths"
wets_downloaded = "outputs/wet_dir"


wets = os.listdir("outputs/wet_dir")
wets = [wet for wet in wets if os.path.getsize(wets_downloaded + "/" + wet) > 1000]
total = [url.strip() for url in open(all_wets).readlines()]

print(len(wets))
print(len(total))


for i, url in enumerate(wets):
    if url in wets:
        print(i)

