def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0,n)]
    sum = signature[:]
    for i in range(3, n):
        sum.append(sum[i-1] + sum[i-2] + sum[i-3])
    return sum

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
print(tribonacci([1, 1, 1], 10))
