def sumDigit(n):
    if n == 0:
        return 0
    return n%10 + sumDigit(n//10)
L = [14,19,125,23]
final_List = []
for num in L:
    final_List.append(sumDigit(num))
print(final_List)