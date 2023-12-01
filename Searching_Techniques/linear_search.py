L=[10,54,98,74,96,34,65]
user=int(input('Enter the user value: '))
for ind in range(len(L)):
  if user == L[ind]:
    print(f'user value present in {ind}')
    break

print(-1)