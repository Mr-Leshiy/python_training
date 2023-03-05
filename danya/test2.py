def bool_and(a, b):
    return a and b
def bool_or(a, b):
    return a or b
def bool_xor(a, b):
    return a ^ b
def bool_not(a):
    return not a
def bool_equal(a, b):
    return a == b
def bool_notequal(a, b):
    return a != b
def bool_grater(a, b):
    return a > b
def bool_less(a, b):
    return a < b
def bool_grater_or_equal(a, b):
    return a >= b
def bool_less_or_equal(a, b):
    return a <= b
def check(x):
    a1 = bool_grater_or_equal(a = x, b = 2)
    a2 = bool_less(a = x, b = 5)
    a3 = bool_and(a= a1, b = a2)
    a4 = bool_notequal(a = x, b =3)
    a5 = bool_and(a = a3, b = a4)
    a6 = bool_equal(a = x, b = 1)
    a7 = bool_or(a = a5, b = a6)
    return a7
d = bool_and(a = True, b = True)
e = bool_and(a = True, b = False)
v = bool_and(a = False, b = False)
c = bool_and(a = False, b = True)
print(d)
print(e)
print(v)
print(c)
print('__')
d = bool_or(a = True, b = True)
e = bool_or(a = True, b = False)
v = bool_or(a = False, b = False)
c = bool_or(a = False, b = True)
print(d)
print(e)
print(v)
print(c)
print('__')
d = bool_not(a = False)
e = bool_not(a = True)
print(d)
print(e)
print('__')
d = bool_xor(a = True, b = True)
e = bool_xor(a = True, b = False)
v = bool_xor(a = False, b = False)
c = bool_xor(a = False, b = True)
print(d)
print(e)
print(v)
print(c)
print('__')
d = bool_equal(a = True, b = True)
e = bool_notequal(a = 4, b = 4)
print(d)
print(e)
print('__')
d = bool_grater(a = 5, b = 2)
e  = bool_less(a = 3, b = 8)
v = bool_grater_or_equal(a =5, b = 5)
c = bool_less_or_equal(a = 4, b = 9)
print(d)
print(e)
print(v)
print(c)
print('__')
x = 4
print(check(x))