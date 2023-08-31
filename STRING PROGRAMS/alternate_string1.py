s = 'abcdef'
newStr = ''
if len(s)%2 == 0:
    
    string1 = s[:len(s)//2]
    string2 = s[len(s)//2:]
else:
    string1 = s[:len(s)//2+1]
    string2 = s[len(s)//2+1:]

for i in range(len(string1)):
    newStr += string1[i]
    newStr += string2[i]

print(newStr)