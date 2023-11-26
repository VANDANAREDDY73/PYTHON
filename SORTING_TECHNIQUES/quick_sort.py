def quick_sort(L):
  if len(L)==0:
    return []
  pivot = L[0]
  left=[num for num in L[1:] if num<pivot]
  right=[num for num in L[1:] if num>pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)
L=[17,5,12,4,7,3,10]
print(quick_sort(L))
 