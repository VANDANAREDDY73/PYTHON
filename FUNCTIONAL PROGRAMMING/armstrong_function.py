def armstrong(num,p,copy,res=0):
    while (num!=0):
        rem = num%10
        res += rem**p
        num //= 10
    return copy == res
num=153
print(armstrong(num,len(str(num)),num))
