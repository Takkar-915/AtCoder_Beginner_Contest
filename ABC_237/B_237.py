H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

At = list(zip(*A))

for i in range(At):
    print(*i)

