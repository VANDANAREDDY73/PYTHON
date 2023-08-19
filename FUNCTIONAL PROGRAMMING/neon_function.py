def neon(num,sq,res=0):
    while (sq != 0):
        rem = sq%10
        res += rem
        sq //= 10
    return num == res
num=9
print(neon(num,sq=num**2))
