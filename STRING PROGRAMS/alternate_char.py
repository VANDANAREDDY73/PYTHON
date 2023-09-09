s = 'axmzw'
ns = ''
for ch in s:
    rem =(ord(ch)-96+3)%26
    if rem == 0:
        ns += 'z'
    else:
        ns += chr(rem + 96)
print(ns)

s = 'agrj'
ns = ''
for ch in s:
    rem =(ord(ch)-96+3)%26
    ns = ns+'z' if rem == 0 else ns+chr(rem+96)
print(ns)
    
    
