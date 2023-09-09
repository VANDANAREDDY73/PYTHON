s = 'a2b3c4a5'
word,num,res = '','',''
for ind in range(len(s)):
    if ind%2 == 0:
        word += s[ind]
    else:
        num += s[ind]
for ind in range(len(word)):
    res += word[ind]*int(num[ind])
print(res)
