m,n,k = map(int,input().split())
z=[];z1=[]
for i in range(m):
    z.append(list(input()))
z1 = [int(i) for i in input().split()]


way =""
x = m-1
y=0

for i in range(k):
    if z1[i] == 0:
        if x-1 >= 0:
            x -= 1
            way += z[x][y]
        else:
            way += z[x][y]
    elif z1[i] == 3:
        if x+1 < m:
            x += 1
            way += z[x][y]
        else:
            way += z[x][y]
    elif z1[i] == 1:
        if y+1 < n:
            y+=1
            way += z[x][y]
        else:
            way += z[x][y]
    elif z1[i] == 4:
        if y-1 >= 0:
            y -= 1
            way += z[x][y]
        else:
            way += z[x][y]
    elif z1[i] == 2:
        if x+1 < m and y+1 < n:
            x += 1
            y += 1
            way += z[x][y]
        else:
            way += z[x][y]
    elif z1[i] == 5:
        if x-1 >= 0 and y-1 >= 0:
            x -=1
            y -=1
            way += z[x][y]
        else:
            way += z[x][y]
print(way)
print(len(set(list(way))))