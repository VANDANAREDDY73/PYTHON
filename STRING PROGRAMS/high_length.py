s = 'aaaaabbbccccccca'
s += '-'
hl = 0
count =1
for ind in range(len(s)-1):
    if s[ind] == s[ind+1]:
        count += 1
        if count > hl :
            hl = count
    else:
        count = 1
print(hl)
