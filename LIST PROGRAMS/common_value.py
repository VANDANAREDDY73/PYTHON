L1 = [11,14,12,13,18]
L2 = [70,11,13,14,50]
newList = []
for num in L1:
    if num in L2:
        newList.append(num)
print(newList)
