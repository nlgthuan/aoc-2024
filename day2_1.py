import sys
infile = sys.argv[1]
inp = open(infile).read().strip()


lines = []
for s in inp.split("\n"):
    lines.append([int(x) for x in s.split()])

count = 0
for l in lines:
    ok = True

    first_diff = l[1] - l[0]
    for i in range(0, len(l) - 1):
        diff = l[i + 1] - l[i]

        if first_diff * diff < 0:
            ok = False
            break

        if abs(diff) < 1 or abs(diff) > 3:
            ok = False
            break

    if ok:
        count += 1



print(count)
