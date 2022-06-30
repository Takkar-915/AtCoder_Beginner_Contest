X,Y = map(int,input().split())

cnt = 0

while(X < Y):
    X += 10
    cnt += 1

print(cnt)