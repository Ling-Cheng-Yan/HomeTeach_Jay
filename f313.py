r,c,k,m = map(int,input().split())

r = r + 2
c = c + 2
p = []
for i in range(r):
    p.append([])

p[0] = [-1] * c
p[r-1] = [-1] * c


for i in range(1, r-1):
    row = [-1]
    input_values = input().split()
    for x in input_values:
        row.append(int(x))
    row.append(-1)
    p[i] = row


temp = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(-1)
    temp.append(row)


for day in range(m):
    for i in range(1,r-1):
        for j in range(1,c-1):
            temp[i][j] = p[i][j]
            if(temp[i][j] < 0):
                continue
            if(p[i-1][j] >= 0):
                temp[i][j] = temp[i][j] + p[i-1][j] // k - p[i][j]//k
            if(p[i+1][j] >= 0):
                temp[i][j] = temp[i][j] + p[i+1][j] // k - p[i][j]//k
            if(p[i][j-1] >= 0):
                temp[i][j] = temp[i][j] + p[i][j-1] // k - p[i][j]//k
            if(p[i][j+1] >= 0):
                temp[i][j] = temp[i][j] + p[i][j+1] // k - p[i][j]//k
    
    temp ,p = p, temp
        

imax = -10000
imin = 1000000

for i in range(r):
    for j in range(c):
        if(p[i][j] > imax):
            imax = p[i][j]
        if(p[i][j] >= 0 and p[i][j] < imin):
            imin = p[i][j]

print(imin)
print(imax)