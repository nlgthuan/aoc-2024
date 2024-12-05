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

def ck(l):
    printed = {}
    for i,n in enumerate(l):
        befores = rules[n]
        for b in befores:
            if b in printed:
                l[i], l[printed[b]] = l[printed[b]], l[i]
                return ck(l)
        printed[n] = i
    return l

ans = 0
for l in ps:
    a = ck(l.copy())
    if a != l:
        ans += a[int(len(a) / 2)]

print(ans)
