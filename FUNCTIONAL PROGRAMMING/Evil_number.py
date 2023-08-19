def evil(num,res=0):
    while (num!=0):
        rem = num%2
        res += rem
        num //= 2
    if (res%2 == 0):
        return True
    return False
num = 27
print(evil(num))
