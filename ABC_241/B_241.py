N,M = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

judge = 0

for i in range(M):
    for j in range(len(A)):
        if B[i] == A[j]:
            A.remove(A[j])
            judge += 1
            break

if judge == M:
    print('Yes')
else:
    print('No')   