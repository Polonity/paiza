row1 = input().split(' ')

min = 0
x = [int(row1[0])]
y = [int(row1[1])]

for i in range(0,int(row1[3])):
    cut = input().split(' ')
    if cut[0] == '0':
        x.append(int(cut[1]))
    if cut[0] == '1':
        y.append(int(cut[1]))


x.sort()
y.sort()

nb = 0
mb = 0
val = 0
for n in x:
    mb = 0
    if (n - nb) != 0:
        for m in y:
            if (m - mb) != 0:
                val = (int(n) - int(nb)) * (int(m) - int(mb))
                if min == 0:
                    min = val
                if min > val:
                    min = val
            mb = m
    nb = n

print (str(min * int(row1[2])))
