year=2021
if (year%100==0):
    if (year%400==0):
        print('LEAP YEAR')
    else:
        print('NON-LEAP YEAR')
else:
    if (year%4==0):
        print('LEAP YEAR')
    else:
        print('NON-LEAP YEAR')
