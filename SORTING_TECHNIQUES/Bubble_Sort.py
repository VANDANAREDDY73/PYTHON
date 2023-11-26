L = [17,5,12,4,7,3,10]
n=len(L)
for ev in range(n-1,0,-1):
  for ind in range(ev):
    if L[ind] > L[ind+1]:
      L[ind],L[ind+1]=L[ind+1],L[ind]
print(L)