def judge(S):
    l = len(S) - len(S.lstrip("a"))
    r = len(S) - len(S.rstrip("a"))
    if l > r:
        return False
    modified_S = "a" * (r-l) + S

    if modified_S == modified_S[::-1]:
        return True
    else:
        return False

S = input()

print("Yes" if judge(S) else "No")
    