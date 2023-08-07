num = 22
print(num)
copy = num
rev = 0
while (num != 0):
    rem = num%10
    rev = rev*10+rem
    num //= 10
if (copy==rem):
    print('Not emirp number')
else:
    count1 = 0
    for fa in range(1,copy+1):
        if (copy%fa==0):
            count1 += 1
    if (count1 == 2):
        count2 = 0
        for fa in range(1,rev+1):
            if (rev%fa == 0):
                count2 += 1
        if (count2 == 2):
            print('Emirp Number')
        else:
            print('Not emirp number')
    else:
        print('Not Emirp Number')
    
