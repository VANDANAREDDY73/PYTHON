def add(n):
    while (n!=1):
        return n+add(n-1)
    return 1
print(add(5))
