import sys

infile = sys.argv[1]
inp = open(infile).read().strip()


ans = 0

m = []
for s in inp.split("\n"):
    m.append([int(x) for x in s])

rows = len(m)
cols = len(m[0])


def fa(r, c):
    a = 0
    q = []
    q.append(tuple([r, c]))
    while len(q) > 0:
        [r, c] = q.pop()

        cur_val = m[r][c]
        if cur_val == 9:
            a += 1
            continue

        # top
        if r - 1 >= 0:
            v = m[r - 1][c]
            if v == cur_val + 1:
                q.append([r - 1, c])
        # right
        if c + 1 < cols:
            v = m[r][c + 1]
            if v == cur_val + 1:
                q.append([r, c + 1])
        # bot
        if r + 1 < rows:
            v = m[r + 1][c]
            if v == cur_val + 1:
                q.append([r + 1, c])
        # left
        if c - 1 >= 0:
            v = m[r][c - 1]
            if v == cur_val + 1:
                q.append([r, c - 1])

    return a


for r in range(rows):
    for c in range(cols):
        if m[r][c] == 0:
            ans += fa(r, c)

print(ans)
