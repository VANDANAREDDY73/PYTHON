s = 'PYTHON'
if len(s)%2 == 0:
    
    string1 = s[:len(s)//2]
    string2 = s[len(s)//2:]
    print('first half of string is ',string1)
    print('second half of string is ',string2)
else:
    string1 = s[:len(s)//2]
    string2 = s[((len(s)//2)+1):]
    print('first half of string is ',string1)
    print('second half of string is ',string2)
    