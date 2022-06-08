list = []

for i in range(7,7777778,7):
    if i %7 == 0:
        list.append(i)


StrA = "".join([str(_) for _ in list])
print(StrA.count('7'))