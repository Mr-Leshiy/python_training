import sys
import math
# a = [6,7,5,4]
# def find_max(a):
#      index = 0
#      max = a[0]
#      index_max = 0
#      while index <= len(a)-1:
#          if a[index]>max:
#              max = a[index]
#              index_max = index
#          index = index + 1
#      return index_max
# while True:
#     b = []
#     for i in range(8):
#         mountain_h = int(input())  # represents the height of one mountain.
#         b.append(mountain_h)
#     print("Debug messages 123", file=sys.stderr, flush=True)
# print(find_max(a))

# def find_max2(a):
#     index = 0
#     max = a[0]
#     while index <= len(a)-1:
#         if a[index]>max:
#             max = a[index]
#         index = index + 1
#     return max

# def find_min2(a):
#     index = 0
#     min = a[0]
#     while index <= len(a)-1:
#         if a[index]<min:
#             min = a[index]
#         index = index + 1
#     return min

a = [4, -1, -3, -9, 6, 1]
def find_close_to(a, value):
    if len(a)==0:
        return 0
    index = 0
    res = a[0]
    while index<len(a):
        if abs(value - a[index]) < abs(value - res):
            res = a[index]
        if abs(value - a[index]) == abs(value - res) and a[index] > res:
            res = a[index]
        index = index + 1
    return res
print(find_close_to(a, 0))
print(find_close_to(a, -10))
print(find_close_to(a, 20))
print(find_close_to([], 0))