import sys
infile = sys.argv[1]
inp = open(infile).read().strip()


left = []
right = []

for s in inp.split("\n"):
    [l, r] = s.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)
