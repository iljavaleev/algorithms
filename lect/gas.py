from decimal import Decimal as decimal
if __name__ == '__main__':
    n = int(input())
    costs = [int(x) for x in input().split()]

    mini = bestB = bestS = maxi = 0
    for i in range(1, n):
        res = decimal(costs[i])/decimal(costs[mini])
        if res > maxi:
            maxi = res
            bestS = i
            bestB = mini
        if costs[i] < costs[mini]:
            mini = i
    if maxi <= 1:
        print(0, 0)
    else:
        print(bestB+1, bestS+1)

