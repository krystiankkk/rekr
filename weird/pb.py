# create the phone book
d = {}
for n in range(int(input())):

    imie,numer = [x.strip() for x in input().strip().split()]
    d[imie]=numer

while True:
    try:
        q = input()

        if q in d:
            print(f"{str(q)}={str(d[q])}")
        else:
            print("Not found")
    except EOFError:
        break
