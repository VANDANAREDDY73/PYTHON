L1 = [11,12,40,76,50]
L2 = [15,11,70,50,12]
for num in L1:
    if num not in L2:
        L2.append(num)
print(L2)
