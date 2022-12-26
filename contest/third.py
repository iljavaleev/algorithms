n = int(input())
data = []
for i in range(n):
    data.append([int(x) for x in input().split()])


n = int(input())
req = []
for i in range(n):
    req.append([int(x) for x in input().split()])

for i in req:
    summ = 0
    long = 0
    if i[-1] == 1:
        for d in data:
            if i[0] <= d[0] <= i[1]:
                summ += d[-1]
                continue
        print(summ, end=' ')

    elif i[-1] == 2:
        for d in data:
            if i[0] <= d[1] <= i[1]:
                long += d[1] - d[0]
                continue
        print(long, end=' ')
