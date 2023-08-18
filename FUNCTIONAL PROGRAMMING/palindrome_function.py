def palindrome(num,copy,rev=0):
    while (num!=0):
        rem = num%10
        rev = rev*10 + rem
        num //= 10
    return copy==rev
num=12321
print(palindrome(num,num))
