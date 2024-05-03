n = int(input())

r = []
for i in range(n):
    r.append(list(map(int,input().split())))

max = -1000000

count = 0
for x,y in r:
    if y > max:
        max = y
        max_idx = x
    if y == -1:
        count = count + 1

score = max - n - 2*count

if score < 0:
    score = 0
print(score,max_idx)


# print(r)