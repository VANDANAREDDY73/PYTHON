L = [10,40,50,'AB',70]
for fi in range(len(L)//2):
    L[fi],L[-fi-1] = L[-fi-1],L[fi]
print(L)
