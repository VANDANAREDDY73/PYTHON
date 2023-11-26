L = [17,5,12,4,7,3,10]
n = len(L)
for ti in range(1,n):
  target = L[ti]
  ind = ti-1
  while ind >= 0 and target < L[ind]:
    L[ind+1] = L[ind]
    ind -= 1
  L[ind+1] = target
print(L)