S = 'ENGINEERING'
while S!='':
    if (S.count(S[0])>1):
        print(S[0])
    S=S.replace(S[0],'')
