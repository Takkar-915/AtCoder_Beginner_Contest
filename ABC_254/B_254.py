N = int(input())

list = []

for n in range(N):    
    list.append([])
    list[n].append(1)
    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])
    if(n != 0):
        list[n].append(1)

for i in range(len(list)):
    print(*list[i])

    