abc = input()

bca = abc[1] + abc[2] + abc[0]

cab = abc[2] + abc[0] + abc[1]

ans = int(abc) + int(bca) + int(cab)

print(ans)