"""円が接しているか否かの判定"""
x1,y1,x2,y2 = map(int,input().split())

r = 5**0.5

distance = ((y2-y1)**2 + (x2-x1)**2)**0.5

standart_line = 2*r

if distance > standart_line:
    print('No')
else:
    print('Yes')
