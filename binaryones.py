def binary(n):
    li=[]
    cnt = 0
    s = bin(n)
    d=s.split('0')
    #print(d)
    for el in d:
        li.append(el.count('1'))
    print(max(li))



binary(13)