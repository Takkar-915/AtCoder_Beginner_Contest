N = int(input())
A = list(map(int,input().split()))

num = []

for i in range(len(A)):
    num.append([])

for j in A:
    num[j].append(j)

for k in range(len(A)):
    if len(num[k]) == 3:
        print(k)

