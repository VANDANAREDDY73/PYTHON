S = 'MALAYALAM'
li = -1
for fi in range(len(S)//2):
    if S[fi] == S[li]:
        li -= 1
    else:
        print('not palindrome')
        break
else:
    print('Palindrome')
