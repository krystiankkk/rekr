def jumping(c):
    jumps = 0
    current = 0

    while current < len(c):
        print(jumps, current)
        
        if current+2 < len(c) and c[current+2] == '0':
            jumps += 1
            current += 2

        elif current+1 < len(c) and c[current+1] == '0':
            jumps += 1
            current += 1
        else:
            current += 1
    return jumps


print(jumping('0010010'))