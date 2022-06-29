N, X = map(int, input().split())

list = []

for i in range(0,27):
    for j in range(N):
        list.append(ord('A')+i)

print(chr(list[X-1]))