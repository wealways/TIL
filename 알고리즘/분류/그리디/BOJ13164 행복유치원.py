import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,K = map(int,input().split())
people = list(map(int,input().split()))

temp = []

for i in range(1,N):
    temp.append(people[i]-people[i-1])
temp.sort()
print(sum(temp[:N-K]))