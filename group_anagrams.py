L=['eat','tea','tan','ate','bat','nat']
res=[]
l1=[]
for ch in L:
  if len(ch)!=len(ch+1):
    res.append(l1)
    l1=[]
  else:
    for i in range(len(L)):
      for j in range(1,range(len(L))):
        if ch.count(i) != ch.count(j):
          ch+=1
        else:
          l1.append(ch)
print(res)

    
    

