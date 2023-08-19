def spy(num,Sum=0,prod=1):
    while (num!=0):
        rem=num%10
        Sum += rem
        prod *= rem
        num //= 10
    return Sum == prod
num=123
print(spy(num))
        
