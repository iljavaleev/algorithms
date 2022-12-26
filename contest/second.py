import datetime
from collections import defaultdict

n = int(input())
data = []
for i in range(n):
    data.append(input().split())

d = defaultdict(list)
for i in data:
    d[i[3]] += [i]

d0 = datetime.date(2021, 1, 1)

for k in d.keys():
    l = sorted(d[k], key=lambda x: x[0])
    for s in l:
        date = datetime.date(2021, 1, 1)
        if s[-1] == 'A':
            date += datetime.timedelta(hours=int(s[1]), minutes=int(s[2]))
        elif s[-1] == "B":
            date += datetime.timedelta(hours=int(s[1]), minutes=int(s[2]))
        else:
            date += datetime.timedelta(hours=int(s[1]),
                                       minutes=int(s[2]))



# inputDate = '21 04 25'
#

#

