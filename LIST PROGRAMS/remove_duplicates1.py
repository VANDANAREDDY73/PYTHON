L = [11,12,11,15,12,15]
newList = []
for num in L:
    if newList.count(num)==0:
        newList.append(num)
print(newList)