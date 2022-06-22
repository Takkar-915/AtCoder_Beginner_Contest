def process(x):
    result = x**2 + 2*x + 3
    return result

t = int(input())

first = process(t)

second = first + t

third = process(second)

forth = process(first)

fifth = process(third + forth)

print(fifth)