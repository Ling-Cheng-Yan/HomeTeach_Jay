k,q,r = map(int,input().split())

word = input()

sortword = []

for i in range(q):
    way = []
    for j in input().split():
        way.append(int(j))
    tempword = ""
    # core algorithm
    for j in range(1,k+1):
        tempword = tempword + word[way.index(j)]
        # "bcaa"
    sortword.append(tempword)
    word = tempword

# print("sortword = ", sortword)
        

for i in range(r):
    for j in sortword:
        print(j[i],end="")
    print()
# print("word = ",word)
# print("way =",way)