def sol(arr, low, high):
    if(len(arr) <= 2):
        return 0
    mid = (low+high) // 2
    d = 0
    small = []
    big = []
    between = set()
    for i in arr:
        if i <= mid:
            d = d + len(between)
            small.append(i)
        else:
            big.append(i)
            if i in between:
                between.remove(i)
            else:
                between.add(i)
    d = d + sol(small,low,mid)
    d = d + sol(big, mid+1,high)
    return d
# main
n = int(input())
a= []
for x in input().split():
    a.append(int(x))

d = sol(a,1,n)
print(d)