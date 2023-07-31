for _ in range(5):
    print('* '*3)

for star in range(5,0,-1):
    print('* '*star)

for star in range(1,5):
    print('* '*star)

star=1
for space in range(4,-1,-1):
    print('-'*space,'*'*star)
    star+=1

space=4
for star in range(1,6):
    print('-'*space,'*'*star,sep=' ')
    space -= 1

space = 0
for star in range(4,0,-1):
    print('-'*space,'*'*star,sep=' ')
    space += 1

star = 4
for space in range(4):
    print('-'*space,'*'*star,sep=' ')
    star -= 1

star = 1
for space in range(4,-1,-1):
    print('-'*space,'*'*star,sep=' ')
    star += 2

star = 7
for space in range(4):
    print('-'*space,'*'*star,sep=' ')
    star -= 2

star = 1
for space in range(3,-1,-1):
    print('-'*space,'*'*star,sep=' ')
    star += 2
else:
    star=5
    for space in range(1,4):
        print('-'*space,'*'*star,sep=' ')
        star -= 2









    



    


