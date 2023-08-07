num = 17
print(num)
#reverse 17
copy = num
rev = 0
while (num != 0):
    rem = num%10
    rev = rev*10+rem
    num //= 10
#count factors for 17
count1 = 0
for fa in range(1,copy+1):
    if (copy%fa == 0):
        count1 += 1
#count factors for 71
count2 = 0
for fa in range(1,rev+1):
    if (rev%fa == 0):
        count2 += 1
#check emirp number or not
if (copy==rev):
    print('not emirp number')
else:
    if (count1==2 and count2==2):
        print('Emirp number')
    else:
        print('Not emirp number')
        
