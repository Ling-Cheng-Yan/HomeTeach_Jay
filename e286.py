# 紀錄 現在A隊 贏幾場
count = 0

# 第一場的A隊的四節分數
scoreA = list(map(int, input().split()))

# 第一場的B隊的四節分數
scoreB = list(map(int, input().split()))

# 第二場的A隊的四節分數
scoreATwo = list(map(int, input().split()))

# 第二場的B隊的四節分數
scoreBTwo = list(map(int, input().split()))

print(str(sum(scoreA)) + ":" + str(sum(scoreB)))

if sum(scoreA) > sum(scoreB):
    count = count + 1

print(str(sum(scoreATwo)) + ":" + str(sum(scoreBTwo)))
if sum(scoreATwo) > sum(scoreBTwo):
    count = count + 1


if count == 2:
    print("Win")
elif count == 1:
    print("Tie")
else:
    print("Lose")