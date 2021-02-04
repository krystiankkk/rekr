i=0
all=[]
mat = '123'
mat1 = '456'
mat2 = '989'
all.append(mat)
all.append(mat1)
all.append(mat2)
d1 = 0
d2 = 0
i = 3
print(all)
for i in range(0, i):
    #print(all[i][i])
    d1 = d1+int(all[i][i])

    #print(all[i][-i-1])
    d2 = d2+int(all[i][-i-1])

print(abs(d1-d2))


def dia(all):
    d1=0
    d2=0
    for i in range(len(arr)):
        d1=d1+int(all[i][i])
        d2=d2+int(all[i][-i-1])
    return abs(d1-d2)
