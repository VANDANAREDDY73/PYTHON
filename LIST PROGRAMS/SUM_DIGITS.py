L = [14, 19, 125, 23]
res = []
for num in L:
    add = 0
    while num != 0:
        rem = num % 10
        add += rem
        num //= 10
    res.append(add)
print(res)
