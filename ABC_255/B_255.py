import numpy as np

N,K = map(int,input().split())
A = list(map(int,input().split()))

xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
l = list(zip(x, y))


dis = 0
max = 0
list = []
for i in A:
    list.append([])
    for j in range(N):
        if i == j:
            list[i].append(0)
        elif i != j:
            o = np.array(l[i])
            p = np.array(l[j])
            dis=np.linalg.norm(p-o)
            list[i].append(dis)  

max_list = []
for a in range(A):
    for b in range(N-1):
        max_list.append(max(list[a][b]))

print(min(max_list))