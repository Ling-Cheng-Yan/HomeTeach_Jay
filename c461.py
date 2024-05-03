num = list(map(int, input().split()))

output = []

if num[0] >= 1:
    num[0] = 1
if num[1] >= 1:
    num[1] = 1

if (num[0] and num[1]) == num[2]:
    output.append("AND")
if (num[0] or num[1]) == num[2]:
    output.append("OR")
if (num[0] ^ num[1]) == num[2]:
    output.append("XOR")

if output:
    for o in output:
        print(o)
else:
    print("IMPOSSIBLE")