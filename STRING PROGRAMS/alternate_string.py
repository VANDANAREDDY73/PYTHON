s='abcdef'
newStr = ''
i=0
j=0
if len(s)%2 == 0:
    
    string1 = s[:len(s)//2]
    string2 = s[len(s)//2:]
else:
    string1 = s[:len(s)//2+1]
    string2 = s[len(s)//2+1:]
while i<len(string1) or j<len(string2):
    

    if i < len(string1):
        newStr += string1[i]
        i += 1
    if j < len(string2):
        newStr += string2[j]
        j += 1
print(newStr)
    