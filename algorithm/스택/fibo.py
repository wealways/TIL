memo=[0,1]

def fibo(n):
    if n>=2 and n>=len(memo):
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

print(fibo(5))