num = 19
if (num>1):
    for fa in range(2,num//2+1):
        if (num%fa == 0):
            print('Not prime')
            break
    else:
        print('prime')
else:
    print('Not prime')
    
