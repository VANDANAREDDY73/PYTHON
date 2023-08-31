num = 8187885813
while num != 0:
    rem = num%10
    count = 0
    for fact in range(1,rem+1):
        if rem%fact == 0:
            count += 1
    if count == 2:
        print(rem)
    num //= 10