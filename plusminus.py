def plusminus(arr):
    plus = 0
    minus = 0
    z = 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            z += 1
    p_rat="%.6f"%(plus/len(arr))
    m_rat = "%.6f"%(minus/len(arr))
    z_rat = "%.6f"%(z/len(arr))
    print(p_rat)
    print(m_rat)
    print(z_rat)
plusminus([1,1,0,-1,-1])