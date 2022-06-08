"""C - Jumping Takahashi 
https://atcoder.jp/contests/abc240/tasks/abc240_c
"""

N,X = map(int,input().split())

#到達できる座標を保持する
position = set()

for i in range(1,N+1):
    a,b = map(int,input().split())

    #新しく到達できる座標
    new_position = set()
    for now in position:
        if now + a <=X:
            new_position.add(now+a)
        elif now + b<=X:
            new_position.add(now+b)
        
    
    position = new_position


if X in position:
    print('Yes')

else:
    print('No')