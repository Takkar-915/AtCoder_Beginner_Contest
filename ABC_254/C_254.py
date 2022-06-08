N,K = map(int,input().split())

a = list(map(int,input().split()))
sorted_a = sorted(a)

flag = False

if a == sorted_a:
  flag = True


for i in range(1,(N-K) + 1):
    copy = a
    copy[i-1],copy[(i-1)+K] = copy[(i-1)+K],copy[i-1]
    
    if copy == sorted_a:
       	flag =True

if flag:
    print('Yes')
else:
    print('No')