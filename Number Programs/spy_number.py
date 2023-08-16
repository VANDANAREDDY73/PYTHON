num=123
Sum=0
prod=1
while(num!=0):
    rem=num%10
    Sum+=rem
    prod*=rem
    num//=10
if (Sum==prod):
    print('spy')
else:
    print('not spy')
    
