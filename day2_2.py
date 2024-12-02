import sys
infile = sys.argv[1]
inp = open(infile).read().strip()


lines = []
for s in inp.split("\n"):
    lines.append([int(x) for x in s.split()])


def is_ok(l):
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

    return ok

count = 0
for l in lines:
    if is_ok(l):
        count += 1
    else:
        for i in range(len(l)):
            sub = l[:i] + l[i+1:]
            ok = is_ok(sub)

            if ok:
                count += 1
                break

print(count)
