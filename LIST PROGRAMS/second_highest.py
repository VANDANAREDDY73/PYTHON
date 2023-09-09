#write a program to print second highest value in the given list.

L = [2,3,10,4,5,2,7,10,8,10,9,11,4]
newList = []
hv = L[0]

for num in L:
    if num not in newList:
        newList.append(num)

shv = newList[0]
for num in L[1:]:
    if num > hv:
        hv = num
for num in newList[1:]:
    if num > shv and num != hv:
        shv = num
print(shv)
