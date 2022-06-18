N = int(input())
A = list(map(int,input().split()))

B = [0,360]
now = 0
for i in A:
    now += i
    now %= 360
    B.append(now)

B.sort()

angle = []

for j in range(len(B)-1):
    sub = B[j+1] - B[j]
    angle.append(sub)

ans = max(angle)
print(ans)