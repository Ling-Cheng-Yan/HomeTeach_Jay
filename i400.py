m,n = map(int,input().split())

#key
e = []
for i in range(m):
    e.append(input())

t = []
for i in input():
    t.append(i)

s = []

for i in range(n):
    s.append("")

#debug
# print("m = ",m,"n = ",n)
# print("t = ", t)
# print("s = ", s)
# print("e = ",e)

# decrypt algorithm

for e_i in e[::-1]:
    nbits = 0
    front = 0
    back = n-1

    for i in range(n):
        if (e_i[i] == "0"):
            s[front]= t[i]
            front = front + 1
        else:
            s[back] = t[i]
            back = back - 1
            nbits = nbits + 1
    
    if nbits % 2 == 1:
        j = n // 2
        if n % 2 == 1:
            j = j + 1
        for i in range(n//2):
            s[i], s[j] = s[j], s[i]
            j = j + 1

    s,t = t,s

print(*t,sep="")