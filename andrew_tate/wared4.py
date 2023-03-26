a = [1]
b = []

# Сортировка пузырьком

def sort_bublle(a):
    if len(a) == 0:
        return None
    progonka = 0
    while progonka < len(a):
        index = 0
        while index < (len(a) - 1 - progonka):
            if a[index] < a[index + 1]:
                lol = a[index + 1]
                a[index + 1] = a[index]
                a[index] = lol
            index += 1
        progonka += 1
    return a

print(sort_bublle(a))

# Поиск макс значения

def find_max_2_0(a):
    indexa = 1
    if len(a) == 0:
        return None
    max = a[0]
    while indexa < len(a):
        if a[indexa] > max:
            max = a[indexa]
        indexa += 1
    return max

print(find_max_2_0(a)) 

# Поиск мин значения

def find_min(a):
    indexa = 0
    if len(a) == 0:
        return None
    min = a[0]
    while indexa < len(a):
        if a[indexa] < min:
            min = a[indexa]
        indexa += 1
    return min

print(find_min(a))

# Поиск макс значения через два цикла

# def find_max(a):
#     indexa = 0
#     while indexa < len(a):
#         indexb = 0
#         flag = True
#         while indexb < len(a):
#             if a[indexa] < a[indexb]:
#                 flag = False
#                 break
#             indexb = indexb + 1 
#         if flag == True:
#                 b.append(a[indexa])
#         indexa = indexa + 1
#     return b[-1]

# #ДЗ: написать для минимума и другой для макса с одним циклом

# !!! QUESTION !!!

# def sort_bublle(a):
#     indexa = 0
#     lol = None
#     while indexa < len(a):
#         indexb = 0
#         while indexb < len(a):
#             if a[indexa] > a[indexb]:
#                 lol = a[indexb]
#                 a[indexb] = a[indexa]
#                 a[indexa] = lol
#                 indexa += 1
#             indexb += 1
#             if indexa == (len(a) - 1):
#                 indexa = 0
#         indexa += 1
#     return a
# print(sort_bublle(a))