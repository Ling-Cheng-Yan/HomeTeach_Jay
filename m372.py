#dstr = ["HFLX","F7IX","H7JX","LIJX"]
def bfs(r,c,mat,m,n):
    que = [(r,c,mat[r][c])]; head = 0
    mat[r][c] = '0'
    while head < len(que):
        r,c,me = que[head]; head += 1
        if c<n-1 and me in "HFLX" and mat[r][c+1] in "H7JX":
            que.append((r,c+1,mat[r][c+1]))
            mat[r][c+1] = '0'
        if c>0 and me in "H7JX" and mat[r][c-1] in "HFLX":
            que.append((r,c-1,mat[r][c-1]))
            mat[r][c-1] = '0'
        if r<m-1 and me in "F7IX" and mat[r+1][c] in "LIJX":
            que.append((r+1,c,mat[r+1][c]))
            mat[r+1][c] = '0'
        if r>0 and me in "LIJX" and mat[r-1][c] in "F7IX":
            que.append((r-1,c,mat[r-1][c]))
            mat[r-1][c] = '0'
            
    return len(que)

m,n = [int(t) for t in input().split()]
mat = []
for i in range(m):
    mat.append(list(input()))
#print(mat)
imax = 0
for i in range(m):
    for j in range(n):
        if mat[i][j]=='0': continue
        imax = max(imax,bfs(i,j,mat,m,n))
#
print(imax)