N = int(input())
H = list(map(int,input().split()))

pos = H[0]

for i in range(N-1):
    if pos < H[i+1]:
        pos = H[i+1]
    else:
        break

print(pos)