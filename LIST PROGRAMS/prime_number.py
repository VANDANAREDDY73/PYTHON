def prime(num,count=0):
    for fa in range(1,num+1):
        if num%fa == 0:
            count += 1
    return count == 2
L = [12,5,7,97,51,23]
for num in L:
    if prime(num):
        print(num)
        