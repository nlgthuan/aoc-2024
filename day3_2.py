import re
import sys
infile = sys.argv[1]
inp = open(infile).read().strip()


p = r"mul\(\d+,\d+\)"
sp = r"\d+"
ans = 0

s = "".join(inp.split("\n"))
s = re.sub(r"don't\(\).*?do\(\)", "----", s)
s = re.sub(r"don't\(\).*", "----", s)

m = (re.findall(p, s))
for a in m:
    [l, r] = (re.findall(sp, a))
    l, r = int(l), int(r)

    ans += l * r

print(ans)
