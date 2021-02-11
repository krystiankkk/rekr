
#print(d1, d2)
lista=[]
for k in range(3):
    i=0
    di=''
    dd=''
    s=input()
    l=[]
    for char in s:
        if i % 2 == 0:
            di+=char
        else:
            dd+=char
        i += 1
    rec=[di, dd]
    lista.append(rec)
print(lista)