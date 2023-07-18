#REMOVE METHOD: This method is used to remove first occurance of given value.
#If value is not in the list, it returns value error.
L = [10,20,15,'abc',(25,26,27),{40,60}]
L.remove(20)
L.remove('abc')
print(L)

#POP METHOD: It removes & returns the value in given index position.
#If index is more than length of the list, it returns index error.
#Providing index is not mandotory & default value as '-1'

S = [10,20,15,'abc',(25,26,27),{40,60}]
S.pop(0)
S.pop(2)
S.pop(7)
print(S)
