S = 'PYTHON'
rev = ''
for ind in range(-1,-len(S)-1,-1):
    rev += S[ind]
if S == rev:
    print('palindrome')
else:
    print('Not palindrome')