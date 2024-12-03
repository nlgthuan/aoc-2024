import re
import sys
infile = sys.argv[1]
inp = open(infile).read().strip()

p = r"mul\(\d{1,3},\d{1,3}\)"
sp = r"\d{1,3}"

ans = 0
for s in inp.split("\n"):
    m = (re.findall(p, s))

    for a in m:
        [l, r] = (re.findall(sp, a))
        l, r = int(l), int(r)

        ans += l * r


print(ans)


