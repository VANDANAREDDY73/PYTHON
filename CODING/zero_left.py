L = [12,0,5,0,18,0,-2,0,3,8]
new_l = []
zero_l = []
for num in L:
    if num != 0:
        new_l.append(num)
    else:
        zero_l.append(num)
print(new_l + zero_l)

finalList = [num for num in L if num!=0]+[num for num in L if num==0]
print(finalList)

finallist = [num for  num in L if num!=0]+[0]*L.count(0)
print(finallist)

finallist = list(filter(lambda num:num!=0,L)) + [0]*L.count(0)
print(finallist)
