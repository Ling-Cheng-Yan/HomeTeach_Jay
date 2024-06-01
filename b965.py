r,c,m=map(int,input().split())


B = []
for i in range(r):
    lst = list(map(int,input().split()))
    B.append(lst)
# print(B)
# [[1,2,3],[2,4,6]]

M = list(map(int, input().split()))

for mm in range(m-1,-1,-1):
    # 翻轉
    if(M[mm]):
        i = 0
        for j in range(r-1,-1,-1):
            if i < j:
                for x in range(c):
                    B[i][x] , B[j][x] =B[j][x], B[i][x]
            i = i + 1
    # 旋轉
    else:
        c_to_r = c - 1
        #A00 = B01
        #A01 = B11
        #A02 = B21
        #A10 = B00
        #A11 = B10
        #A12 = B20
        A = []
        for x in range(c):
            A.append([])

        # print(A)
        for i in range(c):
            for j in range(r):
                A[i].append(B[j][c_to_r-i])
        
        r,c=c,r
        B = A
print(r,c)
for i in range(r):
    first = 1
    for j in range(c):
        if first:
            first = 0
        else:
            print(" ", end="")
        print(B[i][j],end="")
    print()