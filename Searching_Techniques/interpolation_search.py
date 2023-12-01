L=[2,5,8,10,76,569]
user= int(input('Enter the user value : '))
low=0
high=len(L)-1
while low<=high and L[low]<=user<=L[high]:
  ind=int(low+((high-low)/(L[high]-L[low])*(user-L[low])))
  if L[ind] > user:
    high = ind - 1
  elif L[ind] < user:
    low = ind + 1
  elif L[ind]==user:
    print(ind)
    break
else:
  print(-1)