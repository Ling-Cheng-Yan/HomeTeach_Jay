A, B = map(int,input().split())
n = int(input())

t = []
counter = 0

for i in range(n):
    for x in input().split():
        t.append(int(x))
    ca = t.count(A) - t.count(-A)
    cb = t.count(B) - t.count(-B)
    if(ca > 0 and cb > 0):
        counter = counter + 1
    t = []

print(counter)