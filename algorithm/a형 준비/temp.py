
import math

N =123456
primes = [1]*(2*N+1)
primes[0],primes[1] =0,0
for i in range(2,int(math.sqrt(2*N))+1):
    if primes[i]:
        for j in range(2*i,2*N+1,i):
            primes[j]=0

while True:
    M = int(input())
    if M==0:
        break
    print(sum(primes[M+1:2*M+1]))
#
# 246912
#
# sieve = [1]*246913
# sieve[0] = 0
# sieve[1] = 0
# for i in range(2, 246913):
# 	if sieve[i]:
# 		for j in range(i+i, 246913, i):
# 			sieve[j] = 0
# while True:
# 	n = int(input())
# 	if n == 0:
# 		break
# 	print(sum(sieve[n+1:n*2+1]))