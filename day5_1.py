from collections import defaultdict
import sys
infile = sys.argv[1]
inp = open(infile).read().strip()


rules = defaultdict(list)

ps = []

for s in inp.split("\n"):
    if "|" in s:
        [a, b] = s.split("|")
        a, b = int(a), int(b)

        rules[a].append(b)
    elif s != "":
        ps.append([int(x) for x in s.split(",")])

s = 0
for l in ps:
    printed = set()

    vio = False
    for n in l:
        befores = rules[n]
        for b in befores:
            if b in printed:
                vio = True
                break
        if vio:
            break
        printed.add(n)

    if vio == False:
        s += l[int(len(l) / 2)]

print(s)
