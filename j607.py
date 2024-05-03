def addmulti(s):
    multi = 1
    add = 0
    for i in s.split("*"):
        for j in i.split("+"):
            add = add + int(j)
        multi = multi * add
        add = 0
    return multi

def fun1(s):
    val = []
    for i in s.split(","):
        val.append(addmulti(i))
    # print(val)
    return max(val) - min(val)
        

ans = input()

left = []

for i,j in enumerate(ans):
    if j == "(":
        left.append(i)

while left:
    i = left.pop()
    right = ans.index(")",i)
    val = fun1(ans[i+1:right])
    ans = ans[:i-1]+str(val)+ans[right+1:]
    # print(ans)


print((addmulti(ans)))