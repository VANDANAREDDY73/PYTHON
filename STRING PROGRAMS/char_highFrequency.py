S = 'ENGINEERING'
hf = 0
newStr = ''
for ch in S:
    if S.count(ch) > hf:
        hf = S.count(ch)
    if ch not in newStr:
        newStr += ch
for ch in newStr:
    if hf == S.count(ch):
        print(ch)
        