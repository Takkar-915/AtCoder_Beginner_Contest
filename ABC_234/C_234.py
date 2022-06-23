K = int(input())

list = []
while K!= 0  :
    list.append(K % 2)
    K = K //2

list.reverse()

ans = []

for i in list:
    if i == 1:
        i = 2
    ans.append(i)

for s in ans:
    print(s, end = "")
