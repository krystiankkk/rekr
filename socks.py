def sockMerchant(n, ar):
    hash_table = {}
    pair = 0
    for c in ar:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
        if hash_table[c] % 2 == 0:
            pair += 1
    return hash_table, pair


print(sockMerchant(6, [1,1,1,1,1,1,2,3,3,2]))