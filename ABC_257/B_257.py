N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    if A[i-1] < N:
        if not A[i-1]+1 in A:
            A[i-1] += 1

print(*A)