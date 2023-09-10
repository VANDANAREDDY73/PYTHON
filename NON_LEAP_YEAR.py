#write a program to print given year is leap_year or not
#CONDITIONS:
#1-Century leap year is divisible with 400
#2-Non-Century leap year is divisible with 4 and not divisible with 100

#Method -1
year=2021  #Enter the year
if (year%100==0):   
    if (year%400==0):# Checking condition for century leap year
        print('LEAP YEAR')
    else:
        print('NON-LEAP YEAR')
else:
    if (year%4==0): #Checking condition for Non-century leap year
        print('LEAP YEAR')
    else:
        print('NON-LEAP YEAR')

#Method -2
year = 2024
if (year%100 == 0) and (year%400 == 0):
    print('Leap year')
elif (year%4 == 0):
    print('Leap year')
else:
    print('Not leap year')

