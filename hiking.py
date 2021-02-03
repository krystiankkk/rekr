def countingValleys(steps, path):
    alt=0
    VC=0
    for ch in path:
        if ch=='U':
            alt+=1
            if alt ==0:
                VC+=1
        else:
            alt-=1
    return VC
print(countingValleys(8, 'UDDDUDUU'))