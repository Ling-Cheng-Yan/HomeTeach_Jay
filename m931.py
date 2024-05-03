# using sorting to find second largest
n = int(input())
p = []
for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    p.append((x*x+y*y, x, y))
    
# print(p)
p.sort()
# print(p)
print(p[-2][1], p[-2][2])