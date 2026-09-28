prices = [7,1,5,3,6,4]

def trade():
    maxiprofit = 0
    bestbuy = prices[0]
    for i in range(1,len(prices)):
        if prices[i]>bestbuy:
            maxiprofit = max(maxiprofit,prices[i]-bestbuy)
        bestbuy= min(bestbuy,prices[i])

    return maxiprofit

print(trade())