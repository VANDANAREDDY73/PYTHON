L = [11,12,11,15,15,12,15]
newList = []
for num in L:
    if num not in newList:
        newList += [num]
print(newList)
