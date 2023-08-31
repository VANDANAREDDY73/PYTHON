S = 'ENGINEERING'
newStr = '' 
for ch in S:
    if ch not in newStr:
        newStr += ch
for ch in newStr:
    print(f'{ch} = {S.count(ch)}')