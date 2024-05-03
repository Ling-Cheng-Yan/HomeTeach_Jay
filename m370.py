x, n = map(int, input().split())
cntl = 0
cntr = 0
maxv = float('-inf')
minv = float('inf')

for tmp in map(int, input().split()):
    if tmp >= x:
        cntr += 1
    if tmp <= x:
        cntl += 1
    maxv = max(maxv, tmp)
    minv = min(minv, tmp)

if cntl > cntr:
    print(cntl, minv)
else:
    print(cntr, maxv)
