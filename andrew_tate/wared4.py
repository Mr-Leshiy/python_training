# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])

#1) Разбитие на список строк
#2) Перевод строк в целые числа

# Сортировка пузырьком

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

# Поиск индекса макс значения

def find_indexmax(a):
    indexa = 1
    if len(a) == 0:
        return None
    max = a[0]
    indexmax = 0
    while indexa < len(a):
        if a[indexa] > max:
            max = a[indexa]
            indexmax = indexa
        indexa += 1
    return indexmax

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

# Поиск макс значения через два цикла

def find_max(a):
    indexa = 0
    while indexa < len(a):
        indexb = 0
        flag = True
        while indexb < len(a):
            if a[indexa] < a[indexb]:
                flag = False
                break
            indexb += 1 
        if flag == True:
                a.append(a[indexa])
        indexa += 1
    return a[-1]

def find_close_to(a, value):
    if len(a) == 0:
            return 0
    indexc = 0
    res = a[-1]
    while indexc < len(a):
        if abs(a[indexc] - value) < abs(res - value):
            res = a[indexc]
        if abs(a[indexc] - value) == abs(res - value) and a[indexc] > res:
            res = a[indexc]
        indexc += 1
    return res

a = []

print (find_close_to(a, 20))