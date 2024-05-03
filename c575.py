N,K=map(int,input().split())
pos=[int(x) for x in input().split()]
pos.sort()
def check(m):
    now=pos[0]+m
    cnt=1
    for i in pos:
        if i<=now: continue
        cnt+=1
        now=i+m
    return cnt<=K
L=0; R=int(1e9)+1
while R-L>1:
    m=(L+R)//2
    if check(m): R=m
    else: L=m
print(R)