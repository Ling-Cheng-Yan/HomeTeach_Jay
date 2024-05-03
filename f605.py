count, diff = map(int, input().split())
cost = 0
buy = 0
for i in range(count):
    prices = list(map(int, input().split()))
    hprice = max(prices)
    lprice = min(prices)
    if hprice - lprice >= diff:
        cost += sum(prices)//3
        buy += 1

print(buy, cost)