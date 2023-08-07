num = 11
copy = num
rev = 0
while (num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
if (copy == rev):
    count=0
    for fa in range(1,copy+1):
        if (copy%fa==0):
            count += 1
    if (count==2):
        print('Paly Prime')
    else:
        print('NOt Paly Prime')
else:
    print('Not Paly Prime')
