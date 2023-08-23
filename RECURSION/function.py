#write a program to print number from 1 to 10 with the help of recursion
def fun(n):
    if n==11:
        return
    print(n)
    fun(n+1)
fun(1)
