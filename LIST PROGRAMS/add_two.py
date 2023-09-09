L = [5,3,7,2,4]
for num1 in range(len(L)):
    for num2 in range(num1+1,len(L)):
        if L[num1]+L[num2] == 9:
            print(L[num1],L[num2])
            