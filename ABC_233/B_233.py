L,R = map(int,input().split())
S = input()
S_1 = S[L-1:R]

print(S[:L-1] + S_1[::-1] + S[R:])
