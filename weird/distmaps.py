# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
pb={}
for i in range(n):
    x = input()
    l = re.split(' ',x)
    pb[l[0]] = l[1]
        #print(l[0])

while True:
    try:
        check = input()
        if str(check) in pb:
            print(f'{check}={pb[str(check)]}')
        else:
            print('Not found')
    except EOFError:
        pass