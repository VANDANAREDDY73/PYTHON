#Append Method: This method is used to add one value at the end of the given list.
L = [10,20]
L.append(30)
L.append('abc')
L.append((12,13,14))
L.append([50,60,70])
L.append({32,34,36})
L.append({'a':10,'b':20})
print(L)

#insert method: This method is used to add one value at given index position
#if given index is more than length of the list,it will add value at the end of the list.
#if it is positive index , it will add at end of the list.
#if it is negative index , it will add starting of the list.

S = [10,20,30]
S.insert(1,40)
S.insert(2,'abc')
S.insert(7,(12,13,14))
S.insert(-7,{70,80,90})
print(S)

#EXTEND METHOD: This method is used to add multiple values to the given list.
#It takes one argument,which is of iterable (collection data types)(string,tuple,list,set,dict)

N = [10,20]
N.extend((10,20,30))
N.extend([40,40,50])
N.extend({10,10,'abc','v'})
N.extend({'a':10,'b':20,'c':30})
print(N)

