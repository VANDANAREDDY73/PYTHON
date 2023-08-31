S = 'ABCDEF'
if len(S)%2 == 0:
    first_half = S[:len(S)//2]
    second_half = S[len(S)//2:]
    print(first_half,second_half)
else:
    first_half = S[:len(S)//2+1]
    second_half = S[len(S)//2+1:]
    print(first_half,second_half)
