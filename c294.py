while True:
    try:
        t = list(map(int,input().split()))
        # print(t)

        t.sort()
        a = t[0]
        b = t[1]
        c = t[2]
        print(a, b, c)

        if a + b <= c:
            print("No")
        elif a*a + b*b < c*c:
            print("Obtuse")
        elif a*a + b*b == c*c:
            print("Right")
        elif a*a + b*b > c*c:
            print("Acute")
    except:
        break