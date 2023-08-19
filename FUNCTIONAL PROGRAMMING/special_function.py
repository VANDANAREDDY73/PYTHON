def special(num,copy,res=0):
    while (num!=0):
        rem = num%10
        fact=1
        for x in range(1,rem+1):
            fact *= x
        res += fact
        num //= 10
    return copy == res
num=145
print(special(num,num))
