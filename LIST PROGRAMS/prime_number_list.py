#write a program to print prime numbers present in a given list
L = [12,5,7,97,51,23]
for num in L:
    count = 0
    for fact in range(1,num+1):
        if num%fact == 0:
            count += 1
    if count == 2:
        print(num)