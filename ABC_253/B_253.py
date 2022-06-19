H,W = map(int,input().split())
a = [input() for _ in range(H)]

x = []
y = []
ans = 0

for k in range(H):
    for l in range(W):
        if a[k][l] == "o":
            x.append(k)
            y.append(l)

abs_x = abs(x[1]-x[0])
abs_y = abs(y[1]-y[0])
ans = abs_x + abs_y
print(ans)