s = 'abcd'
newStr = ''
for ch in s:
    newStr += chr(ord(ch)+1)
print(newStr)