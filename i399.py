lst = []

for i in input().split():
    lst.append(i)

lst.sort()

# print(lst)

if(lst[0] == lst[2]):
    print(3,lst[0])
elif (lst[0] == lst[1] or lst[1] == lst[2]):
    print(2,lst[2],lst[0])
else:
    print(1,lst[2],lst[1],lst[0])