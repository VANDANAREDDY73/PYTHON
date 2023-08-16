num = 9
sq = num**2
res = 0
while (sq!=0):
    rem=sq%10
    res+=rem
    sq//=10
if (num==res):
    print('neon number')
else:
    print('not neon number')
