num = 25
sq = num**2
p=len(str(num))
rem=sq%(10**p)
if (num==rem):
    print('Automophic number')
else:
    print('Not automorphic number')
    

