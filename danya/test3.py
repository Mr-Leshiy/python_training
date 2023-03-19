a = range(2, 1000)
index = 0
check = index <= len(a) - 1
# # for i in a:
# #     if i % 2 != 0:
# #         print(i)
# len(a)
# print(a[0])
# a[1000]
# print(len(a) - 1)
# while True:
#     print("Bye")
# while True or False:
#     print("Hello")
while check:
    b = a[index]
    if b % 2 == 0:
        print(b)
    index = index + 5
    check = index <= len(a) - 1