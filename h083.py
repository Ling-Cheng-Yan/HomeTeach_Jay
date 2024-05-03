 
n = int(input())
G = []
for i in range(n):
  ji = input()
  G.append(ji)
 
S = set(G)
ans = 0
for i in G:
  for j in range(1, len(i)//2+1):
    if i[:j] == i[-j:]:
      if i[j:-j] in S:
        ans += 1
print(ans)