a = [2, 4, 1, 5]

#index = 0
# while index <= len(a)-1:
#     print(a[index])
#     index = index + 1

# def find_max(a):
#     index = 0
#     max = a[0]
#     while index <= len(a)-1:
#         if a[index]>max:
#             max = a[index]
#         index = index + 1
#     return max

# def find_min(a):
#     index = 0
#     min = a[0]
#     while index <= len(a)-1:
#         if a[index]<min:
#             min = a[index]
#         index = index + 1
#     return min

# print(find_max(a))
# print(find_min(a))

def sort(a):
    p = 0
    while p <= len(a)-1:
        index = 0
        while index < len(a)-1:
            if a[index]>a[index+1]:
                b = a[index]
                a[index] = a[index+1]
                a[index+1] = b
            index = index + 1
        p = p + 1
    return a

def sort2(a):
    p = 0
    while p <= len(a)-1:
        index = 0
        while index < len(a)-1:
            if a[index]<a[index+1]:
                b = a[index]
                a[index] = a[index+1]
                a[index+1] = b
            index = index + 1
        p = p + 1
    return a

print(sort(a))
print(sort2(a))