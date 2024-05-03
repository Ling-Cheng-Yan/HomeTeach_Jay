input1 = input()

input2 = input()

n = int(input())

tmp1 = input1.split()

tmp2 = input2.split()

A1 = int(tmp1[0])

A2 = int(tmp2[0])

B1 = int(tmp1[1])

B2 = int(tmp2[1])

C1 = int(tmp1[2])

C2 = int(tmp2[2])

Y1 = 0

Y2 = 0;  

totals = []

for i in range(n+1):

     X1 = i

     X2 = n-X1

     Y1 = A1*X1*X1+B1*X1+C1

     Y2 = A2*X2*X2+B2*X2+C2

     

     totals.append(Y1+Y2)

     



print(max(totals))