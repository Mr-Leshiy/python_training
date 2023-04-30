def fact(n):
    if n==1:
        return 1
    if n < 0:
        return None
    return n*fact(n-1)

def fact2(b):
    index = 1
    res = 1
    while index <= b:
        res = res*index
        index += 1
    return res

def Fibonacci(a):
    if a < 0:
        return None
    if a==0:
        return 0
    if a==1:
        return 1
    if a>=2:
        return Fibonacci(a-1)+Fibonacci(a-2)
    
def Fib(c):
    if c==0:
        return 0
    if c==1:
        return 1
    index = 1
    f_n = 1
    f_n_1 = 0
    while index<c:
        f_n = f_n + f_n_1
        f_n_1 = f_n - f_n_1
        index += 1
        res = f_n
    return f_n

print(fact(3))
print('____')
print(fact2(5))
print('____')
a = 17
print(Fibonacci(a))
print('____')
c = 32
print(Fib(c))