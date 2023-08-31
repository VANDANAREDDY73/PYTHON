S = 'AVENGERS'
newStr = ''
for ch in S:
    if ch not in 'aeiouAEIOU':
        newStr += ch
print(newStr)