num = 121
copy = num
rev = 0
while (num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
if (copy==rev):
    print('Palindrome')
else:
    print('Not Palindrome')
