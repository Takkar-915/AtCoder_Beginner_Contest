def judge():

    def f(xa,ya,xb,yb):
        return (xa - xb) ** 2 + (ya - yb) ** 2

    x1,y1,x2,y2 = map(int,input().split())

    for i in range(-2,3):
        for j in range(-2,3):
            xt = x1 + i
            yt = y1 + j

            if f(xt,yt,x1,y1) == 5 and f(xt,yt,x2,y2) == 5:
                return True
    return False

print('Yes' if judge() else 'No')