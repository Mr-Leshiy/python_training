n = -3
def fact(n):
    if n==1:
        return 1
    if n < 0:
        return None
    return n*fact(n-1)

print(fact(n))
print('_____')
a = 3
def Fibonacci(a):
    if a < 0:
        return None
    if a==0:
        return 0
    if a==1:
        return 1
    if a>=2:
        return Fibonacci(a-1)+Fibonacci(a-2)
print(Fibonacci(a))