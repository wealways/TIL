def counting_sort(A,B,k):
    C = [0] * (k+1)
    # 카운팅
    for i in range(len(B)):
        C[A[i]] += 1
    # 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]
    # 소트 결과
    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1




a = [0,4,1,3,1,2,4,1]
b = [0] * len(a)
counting_sort(a,b,10)

print(a)
print(b)

