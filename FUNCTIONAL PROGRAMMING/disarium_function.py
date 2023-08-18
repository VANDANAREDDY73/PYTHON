def disarium(num,p,copy,res=0):
    while (num!=0):
        rem = num%10
        res += rem**p
        num //= 10
        p -= 1
    return copy == res
num=135
print(disarium(num,len(str(num)),num))
