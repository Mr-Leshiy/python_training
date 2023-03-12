# a = [1, True, False, "String", 5, 7, None]

# for i in a:
#     print(i)

b = range (0, 100)
index = 0

# for i in b:
#     if i%2 == 0:
#         print(i)

check = index <= (len(b) - 1)

while check:
    if b[index] %2 == 0:
        print(b[index])
    index = index + 4
    check = index <= (len(b)-1)