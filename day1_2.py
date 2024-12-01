import sys

infile = sys.argv[1]
inp = open(infile).read().strip()

left = []
count = {}

for s in inp.split("\n"):
    [l, r] = s.split()
    left.append(int(l))
    num = int(r)
    count[num] = count.get(num, 0) + 1

score = 0
for n in left:
    if n in count:
        score += n * count[n]

print(score)
