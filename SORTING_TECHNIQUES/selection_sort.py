L = [17,5,12,4,7,3,14]
n = len(L)
for ti in range(n-1):
  li=ti
  for ind in range(ti+1,n):
    if L[ind] <  L[li]:
      li=ind
  L[li],L[ti] = L[ti],L[li]
print(L)