def prime(num,count=0):
    for fa in range(1,num+1):
        if (num%fa==0):
            count += 1
    return count == 2
def palindrome(num,copy,rev=0):
    while (num!=0):
        rem = num%10
        rev = rev*10 + rem
        num //= 10
    return copy == rev

        
def palyprime(num):
    return palindrome(num,num) and prime(num)
num = 11
print(palyprime(num))
    
