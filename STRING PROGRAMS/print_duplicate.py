S = 'ENGINEERING'
newStr = ''
for ch in S:
    if ch not in newStr:
        newStr += ch
        if S.count(ch)>1:
            print(ch)
            