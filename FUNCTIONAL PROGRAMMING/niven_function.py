def niven(num,copy,add=0):
    while (num!=0):
        rem = num%10
        add += rem
        num //= 10
    return copy%add==0
num=12
print(niven(num,num))
