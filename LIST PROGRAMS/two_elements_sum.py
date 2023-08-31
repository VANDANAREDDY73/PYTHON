# write a program to print two numbers sum is 5 by taking two elements from given list
L = [2,3,1,4,6]
for num1 in range(len(L)):
    for num2 in range(num1+1,len(L)):
        if L[num1] + L[num2] == 5:
            print(L[num1], L[num2])