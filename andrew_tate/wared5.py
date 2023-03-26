def factorial(a):
    if a == 1:
        return 1
    if a < 0:
        return None
    return a * factorial(a-1)

print(factorial(-5))

def fibonachi(a):
    if a < 0:
        return None
    if a == 1:
        return 0
    if a == 2:
        return 1
    return (fibonachi(a-1) + fibonachi(a-2))

print(fibonachi(10))

# def factorial_2_0(a):
#     b = range(1, a)
#     for i in b:

#     return a

# print(factorial_2_0(3))