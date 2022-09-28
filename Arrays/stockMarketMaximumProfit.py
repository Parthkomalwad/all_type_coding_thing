prices = list(map(int, input()))
maximum_profit = 0
right = 1
left = 0
while right < len(prices):
    current_profit = prices[right] - prices[left]
    if(prices[left] < prices[right]):
        maximum_profit = max(current_profit, maximum_profit)
    else:
        left = right
    right += 1
print(maximum_profit)
