R,C = map(int,input().split())

A1 = list(map(int,input().split()))

A2 = list(map(int,input().split()))

if R == 1 and C ==1:
    print(A1[0])
elif R == 1 and C ==2:
    print(A1[1])
elif R == 2 and C ==1:
    print(A2[0])
else:
    print(A2[1])