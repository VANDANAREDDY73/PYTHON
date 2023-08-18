def prime(num,count=0):
    for fa in range(1,num+1):
        if num%fa == 0:
            count += 1
    return count == 2
num=3
print(prime(num))
