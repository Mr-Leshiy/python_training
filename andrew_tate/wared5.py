def factorial(a):
    if a == 1:
        return 1
    if a < 0:
        return None
    return a * factorial(a-1)

def fibonachi(a):
    if a < 0:
        return None
    if a == 1:
        return 0
    if a == 2:
        return 1
    return (fibonachi(a-1) + fibonachi(a-2))

def fib_2_0(a):
    index = 2
    fn_1 = 0
    fn = 1
    if a == 0:
        return 0
    if a == 1:
        return 1
    while index < a:
        fn = fn + fn_1
        fn_1 = fn - fn_1
        index += 1
    return fn

def factorial_2_0(a):
    index = 1
    result = 1
    while index <= a:
        result *= index
        index += 1
    return result

def sort_bublle(a):
    if len(a) == 0:
        return None
    progonka = 0
    while progonka < len(a):
        index = 0
        while index < (len(a) - 1 - progonka):
            if a[index] > a[index + 1]:
                lol = a[index + 1]
                a[index + 1] = a[index]
                a[index] = lol
            index += 1
        progonka += 1
    return a

def dz(a):
    if a == 0:
        return 1
    index = 1
    fn_1 = 1
    fn = 2
    while index < a:
        fn = fn * fn_1
        fn_1 = fn / fn_1
        index += 1
    return int(fn)

def dz_2(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        return 1
    index = 2
    fn = None
    fn_1 = 1
    fn_2 = 1
    fn_3 = 0
    while index < a:
        fn = fn_1 + fn_2 + fn_3
        fn_3 = fn_2
        fn_2 = fn_1
        fn_1 = fn
        index += 1
    return int(fn)
        
print(dz(5))
print(dz_2(5))