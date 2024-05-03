count = int(input())
score = list(map(int, input().split()))

ispass = []
unpass = []

for i in range(count):
    if score[i] >= 60:
        ispass.append(score[i])
    else:
        unpass.append(score[i])

score.sort()
ispass.sort()
unpass.sort()

for s in score:
    print(s, end=" ")

print()

if unpass:
    print(unpass[-1])
else:
    print("best case")

if ispass:
    print(ispass[0])
else:
    print("worst case")