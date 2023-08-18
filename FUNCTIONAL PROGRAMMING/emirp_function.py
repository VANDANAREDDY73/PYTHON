def prime(num,count=0):
    for fa in range(1,num+1):
        if (num%fa==0):
            count += 1
    return count == 2
def reverse(num,rev=0):
    while (num!=0):
        rem = num%10
        rev = rev*10 + rem
        num //= 10
    return rev

        
def emirp(num):
    return num != reverse(num) and prime(num) and prime(reverse(num))
num = 17
print(emirp(num))
    
