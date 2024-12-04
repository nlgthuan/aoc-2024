import sys
infile = sys.argv[1]
inp = open(infile).read().strip()

a = []

req = ["XMAS", "SAMX"]

ans = 0

for s in inp.split("\n"):
    a.append(list(s))

rows = len(a)
cols = len(a[0])

for r in range(rows):
    for c in range(cols):
        if r+3 < rows and c < cols:
            if "".join([a[r][c], a[r+1][c], a[r+2][c], a[r+3][c] ]) in req:
                ans += 1

        if r < rows and c+3 < cols:
            if "".join([a[r][c], a[r][c+1], a[r][c+2], a[r][c+3]]) in req:
                ans += 1

        if r+3 < rows and c+3 < cols:
            if "".join([a[r][c], a[r+1][c+1], a[r+2][c+2], a[r+3][c+3]]) in req:
                ans += 1

        if r + 3 < rows and c - 3 >= 0:
            if "".join([a[r][c], a[r+1][c-1], a[r+2][c-2], a[r+3][c-3]]) in req:
                ans += 1



print(ans)
