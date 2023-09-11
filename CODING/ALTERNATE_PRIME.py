#write a code to print alternate prime numbers from 1 to 20
L=[]
for num in range(1,21):
    if len([fa for fa in range(1,num+1) if num%fa==0])==2:
        L.append(num)
print(L[::2])
                  
