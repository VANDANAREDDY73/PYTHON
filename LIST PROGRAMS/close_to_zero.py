L = [-9,7,2,7,-6]
closest = L[0]
min_distance = abs(L[0])
for num in L:
    distance = abs(num)
    if distance < min_distance:
        min_distance = distance
        closest = num
print(closest)
    
    
