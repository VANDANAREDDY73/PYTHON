def merge_sort(L):
  if len(L) <= 1:
    return L
  mid = len(L)//2
  left_half = L[:mid]
  right_half=L[mid:]
  merge_sort(left_half)
  merge_sort(right_half)
  merge(L,left_half,right_half)
def merge(L,left,right):
  ind=li=ri=0
  while li<len(left) and ri<len(left):
    if left[li] < right[ri]:
      L[ind] = left[li]
      li+=1
    else:
      L[ind] = right[ri]
      
      ri+=1
    ind += 1
  while ri<len(right):
    L[ind]=right[ri]
    ind+=1
    ri+=1
  while li<len(left):
    L[ind]=left[li]
    ind+=1
    li+=1
L=[17,5,12,4,7,3,10]
merge_sort(L)
print(L)
