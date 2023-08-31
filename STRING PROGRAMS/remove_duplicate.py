s= 'ENGINEERING'
newStr = ''
for ch in s:
    if newStr.find(ch) == -1:
        newStr += ch
print(newStr)