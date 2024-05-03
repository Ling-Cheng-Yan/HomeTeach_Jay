s, t, n, m, r = map(int, input().split())

A = []
B = []

A_sum = 0
for i in range(s):
    row = list(map(int, input().split()))
    A.append(row)
    A_sum += sum(row)

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

total = 0
minn = float('inf')
for i in range(n - s + 1):
    for j in range(m - t + 1):
        not_same = 0
        small_sum = 0
        for y in range(s):
            for z in range(t):
                if B[y + i][z + j] != A[y][z]:
                    not_same += 1
                small_sum += B[y + i][z + j]

        if not_same <= r:
            total += 1
            diff = abs(small_sum - A_sum)
            if diff < minn:
                minn = diff

print(total)
if total == 0:
    print(-1)
else:
    print(minn)
