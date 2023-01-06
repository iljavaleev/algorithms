l = [250, 270, 230, 240, 222, 260, 294, 210]
l = [0, 10, 20, 30, 40, 50, 60, 70]
l = [70, 60, 50, 40, 30, 20, 10, 0]
l = []

def max_revenue(prices):
    if not prices:
        return 0

    min = prices[0]
    max_diff = 0

    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        else:
            if prices[i] - min > max_diff:
                max_diff = prices[i] - min

    return max_diff

print(max_revenue(l))