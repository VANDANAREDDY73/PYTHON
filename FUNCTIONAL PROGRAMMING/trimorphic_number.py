def trimorphic(num,cub,p):
    rem = cub%(10**p)
    return num == rem
num=6
print(trimorphic(num,cub=num**3,p=len(str(num))))
