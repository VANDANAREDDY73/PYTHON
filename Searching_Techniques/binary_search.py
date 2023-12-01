L=[1,5,34,76,84,99,768]
user=int(input('Enter the user value: '))
low=0
high=len(L)-1
while low<=high:
  mid=(low+high)//2
  if L[mid] > user:
    high = mid-1
  elif L[mid] < user:
    low = mid + 1
  elif L[mid] == user:
    print(mid)
    break
else:  
  print(-1)