from functools import reduce
from operator import add
n = int(input())
data = []
for i in range(n):
    data.append(input().split(','))

dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
        'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,
        'v':22,'w':23,'x':24,'y':25,'z':26}

for d in data:
    symb = len(set(''.join(d[:3])))
    dr = reduce(add, [int(x) for x in list(d[3]) + list(d[4])]) * 64
    alph_ord = dict[d[0][0].lower()] * 256
    print(f'{symb + dr + alph_ord:0>3X}'[-3:], end=' ')


