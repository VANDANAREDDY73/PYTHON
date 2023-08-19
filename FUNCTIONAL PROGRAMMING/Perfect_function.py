def perfect(num,Sum=0):
    for fa in range(1,(num//2)+1):
        if num%fa==0:
            Sum += fa
    return num == Sum
num = 6
print(perfect(num))
