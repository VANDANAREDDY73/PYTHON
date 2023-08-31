s = 'we are in job we are in job are we job job'
L = s.split()
hL = 0
newL = []
for word in L:
    if L.count(word) > hL:
        hL = L.count(word)
    if word not in newL:
        newL.append(word)
for word in newL:
    if L.count(word) == hL:
        print(word)
    