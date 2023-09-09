s = 'Hello World!'
upper_s = ''
for ch in s:
    if 'a'<=ch<='z':
        upper_ch = chr(ord(ch)-32)
        upper_s += upper_ch
    else:
        upper_s += ch
print(upper_s)