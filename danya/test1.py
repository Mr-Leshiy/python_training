def sum(j, e):
    return j + e
def sub(j, e):
    return j - e
def mul(j, e):
    return j * e
def div(j, e):
    return j / e
a = 5
b = 'c'
c = True
d = "hello"
print(a)
print(b)
print(c)
print(d)
e = a
a = d
d = e
print(a)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a1 = type(a)
b1 = type(b)
c1 = type(c)
d1 = type(d)
print(type(a1), type(b1), type(c1), type(d1))
h = 1
f = 2
g = sum(e = 2, j = 3)
w = sub(e = 4, j = 1)
x = mul(e = 4, j = 5)
y = div(e = 15, j = 3)
print(g)
print(w)
print(x)
print(y)