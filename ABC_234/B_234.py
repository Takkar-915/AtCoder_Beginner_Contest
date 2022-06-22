"""もう一回やる"""
def solve():
    ans = 0
    for i in range(N):
        x1, y1 = XY[i]
        for j in range(i):
            x2, y2 = XY[j]
            l = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            ans = max(ans, l)
    return ans


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
print(solve())