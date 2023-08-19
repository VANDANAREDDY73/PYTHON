def automorphic(num,sq,p):
    rem = sq%(10**p)
    return num == rem
num=25
print(automorphic(num,sq=num**2,p=len(str(num))))
