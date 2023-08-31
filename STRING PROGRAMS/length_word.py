S = 'WE ARE IN JOB'
L = S.split()
hL = 0
newL = []
for word in L:
    if len(word) > hL:
        hL = len(word)
    if word not in newL:
        newL.append(word)
for word in newL:
    if len(word) == hL:
        print(word)