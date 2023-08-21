def prime(num,count=0):
    for fa in range(1,num+1):
        if num%fa == 0:
            count += 1
    return count == 2
num=2
count=0
while (not count == 5):
    if prime(num):
        count+=1
        print(num)
    num+=1


    
