def multiply(n):
    results=[]
    for i in range(1,11):
        res= i*int(n)
        results.append(res)
    return results


print(multiply(input()))