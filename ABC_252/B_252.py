"""B - Takahashi's Failure"""
N,K = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

max_value = max(A)
flag = False

for i in range(K):
    if A[B[i]-1] == max_value:
        flag = True

if flag:
    print('Yes')
else:
    print('No')