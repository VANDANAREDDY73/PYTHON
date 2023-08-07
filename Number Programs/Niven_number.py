num = 12
copy = num
add = 0
while (num != 0):
    rem = num%10
    add += rem
    num //= 10
if (copy%add == 0):
    print('Niven')
else:
    print('Not Niven')
    
