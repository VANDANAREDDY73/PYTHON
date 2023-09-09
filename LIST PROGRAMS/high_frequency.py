L = [11,11,11,11,14,12,13,18,11,14,12,12,11,12]
hf = 0
newList = []
for num in L:
    if L.count(num)>hf:
        hf = L.count(num)
    if num not in newList:
        newList.append(num)
for num in newList:
    if hf == L.count(num):
        print(num)
