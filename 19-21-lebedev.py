#!/usr/bin/python
#Пример для условия что увеличение на 1, увеличение на 3, увеличение в 4 раза. пока в куче <=58 камней
ee = [59]
N = set(range(1, ee[0]))
L, W = set([ee[0]]), set()
for i in range(20):
    Q = N.copy()
    R = set()
    for x in N:
        if i % 2 == 0:
            if (x + 1) in L or (x + 3) in L or (x * 4) in L or (x * 4) > ee[0]:
                Q -= set([x])
                W = W.union(set([x]))
                R = R.union(set([x]))
        else:
            if (x + 1) in W and (x + 3) in W and (x * 4) in W:
                L = L.union(set([x]))
                Q -= set([x])
                R = R.union(set([x]))
    print(i, R)
    N = Q
