n,m = map(int,input().split())

x = [0]
for i in input().split():
    x.append(int(i))
y = [0]
for i in input().split():
    y.append(int(i))

alive = []
for i in input().split():
    alive.append(int(i))

n_lose = [0]*(n+1)

while(len(alive)>1):
    winner = []
    loser = []
    for i in range(0,len(alive)-1,2):
        first,second = alive[i], alive[i+1]
        a,b,c,d = x[first], y[first], x[second], y[second]
        if a*b >= c*d:
            win = first
            x[first] = x[first] + c*d//(2*b)
            y[first] = y[first] + c*d//(2*a)
            lose = second
            x[second] = x[second] + c//2
            y[second] = y[second] + d//2
        else:
            win = second
            x[second] = x[second] + a*b//(2*d)
            y[second] = y[second] + a*b//(2*c)
            lose = first
            x[first] = x[first] + a//2
            y[first] = y[first] + b//2
        winner.append(win)
        n_lose[lose] = n_lose[lose] + 1
        if n_lose[lose] < m:
            loser.append(lose)
    
    if(len(alive)%2==1):
        winner.append(alive[-1])
    alive = winner + loser
    
print(alive[0])