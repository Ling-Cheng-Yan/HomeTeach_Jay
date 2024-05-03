count = int(input())
wall = list(map(int, input().split()))

sum = 0
for i in range(1, count-1):
    if wall[i] == 0:
        target = min(wall[i-1], wall[i+1])
        sum += target
if wall[0] == 0:
    sum += wall[1]
if wall[-1] == 0:
    sum += wall[-2]

print(sum)