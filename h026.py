# 贏的方式
# 0 是 石頭
# 2 是 剪刀
# 5 是 布
# 0 2 -> 0
# 2 5 -> 2
# 5 0 -> 5

# 哥哥出的拳
brother = int(input())
# 接下來比幾輪
n = int(input())
# 妹妹出的拳，轉成陣列，比較好之後去做比較
sisterType = list(map(int, input().split()))


for i in range(0, n):
    print(brother, end=" ")
    # 兩個如果出一樣的，這個回合平手
    if brother == sisterType[i]:
        # 決定哥哥下次要出的拳
        if i > 0 and sisterType[i] == sisterType[i-1]:
            if sisterType[i] == 0:
                brother = 5
            if sisterType[i] == 2:
                brother = 0
            if sisterType[i] == 5:
                brother = 2
        else:
            brother = sisterType[i]
        continue

    # 妹妹出剪刀
    if sisterType[i] == 2:
        if brother == 0:
            print(": Won at round", i+1)
        else:
            print(": Lost at round", i+1)
        break

    # 妹妹出石頭
    if sisterType[i] == 0:
        if brother == 5:
            print(": Won at round", i+1)
        else:
            print(": Lost at round", i+1)
        break

    # 妹妹出布
    if sisterType[i] == 5:
        if brother == 2:
            print(": Won at round", i+1)
        else:
            print(": Lost at round", i+1)
        break






else:
    print(": Drew at round", n)