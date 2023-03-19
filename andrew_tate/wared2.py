def bool_and (a, b):
    c = a and b
    return c

def bool_or (a, b):
    c = a or b
    return c

def bool_xor (a, b):
    c = a ^ b
    return c

def bool_not (a):
    c = not a
    return c

def equal (a, b):
    c = a == b
    return c

def not_equal (a, b):
    c = a != b 
    return c

def greater (a, b):
    c = a > b
    return c

def greater_equal (a, b):
    c = a >= b
    return c

def less (a, b):
    c = a < b
    return c

def less_equal (a, b):
    c = a <= b
    return c

def check (a):
    c = equal(a=a, b=1) or greater_equal(a=a,b=2) and not_equal(a=a, b=3) and less(a=a,b=5)
    return c

def check2 (a):
    if a == 1 or a >= 2 and a != 3 and a < 5:
        print("a Принадлежит промежутку и равняется:", a)
    else:
        print("a Не принадлежит промежутку и равняется:", a)
    

# print(bool_and(True, True))
# print(bool_and(True, False))
# print(bool_and(False, False))
# print(bool_and(False, True))

# print("-----------------")

# print(bool_or(True, True))
# print(bool_or(True, False))
# print(bool_or(False, False))
# print(bool_or(False, True))

# print("-----------------")

# print(bool_not(True))
# print(bool_not(False))

# print("-----------------")

# print(bool_xor(True, True))
# print(bool_xor(True, False))
# print(bool_xor(False, False))
# print(bool_xor(False, True))

# print("-----------------")

# print(not_equal(2,2))
# print(equal(2,2))
# print(not_equal(True,True))
# print(equal(True,True))
# print(not_equal("123","123"))
# print(equal("123","123"))

# print("-----------------")

# print(greater(5, 4))
# print(greater_equal(5, 6))
# print(less(8, 10))
# print(less_equal(8,8))

# print("-----------------")

check2(10)

# a = False and (False or True)
# print(a)