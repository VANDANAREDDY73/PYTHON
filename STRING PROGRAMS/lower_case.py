s = 'Hello World!'
lower_s = ''
for ch in s:
    if 'A' <= ch <= 'Z':
        lower_ch = chr(ord(ch)+32)
        lower_s += lower_ch
    else:
        lower_s += ch
print(lower_s)
