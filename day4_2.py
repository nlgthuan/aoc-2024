import sys
infile = sys.argv[1]
inp = open(infile).read().strip()

a = []

req = ["MAS", "SAM"]

ans = 0

for s in inp.split("\n"):
    a.append(list(s))

rows = len(a)
cols = len(a[0])

for r in range(rows):
    for c in range(cols):
        if r + 2 < rows and c + 2 < cols:
            if "".join([a[r][c], a[r+1][c+1], a[r+2][c+2]]) in req and "".join([a[r][c+2], a[r+1][c+1], a[r+2][c]]) in req:
                ans += 1



print(ans)
