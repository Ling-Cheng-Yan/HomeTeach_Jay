n,d = map(int,input().split())
a = []
for i in input().split():
    a.append(int(i))

flag = 1

buy = a[0]
profit = 0
sold = 100000000

for i in range(1,n):
    if flag:
        if(a[i] >= buy+d):
            profit = profit + (a[i] - buy)
            sold = a[i]
            flag = 0
    else:
        if(a[i] <= sold-d):
            buy = a[i]
            flag = 1

print(profit)
        

