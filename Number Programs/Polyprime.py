num = 11
#reverse 17
copy = num
rev = 0
while (num!=0):
    rem=num%10
    rev=rev*10+rem
    num //= 10
#count factors for 17
count = 0
for fa in range(1,copy+1):
    if (copy%fa==0):
        count += 1

#check poly prime or not
if (copy==rev and count==2):
    print('Paly Prime')
else:
    print('Not Paly Prime')
