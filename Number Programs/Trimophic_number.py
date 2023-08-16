num = 6
cub = num**3
p = len(str(num))
rem = cub%(10**p)
if (num%rem):
    print('Trimorphic Number')
else:
    print('Not trimorphic number')
