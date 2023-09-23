l1 = [[2,3],[4,5]]
l2 = ['best','wishes']
t = ()
for i in range (len(l2)):
    x = l2[i]
    for j in range(len(l2)):
        if x == 'best' and l1[j] == [2,3]:
            for k in range(len(l1[j])):
                        t = t + (x,l1[j][k])
print(t)