a = [1,1,2,2,3,3,4,4,5,5,6,6,7,7]
b = []
def bubble_sort(a):
    index = 0
    while index < len(a):
        
        index = index + 1

def find_max(a):
    indexa = 0
    while indexa < len(a):
        indexb = 0
        flag = True
        while indexb < len(a):
            if a[indexa] < a[indexb]:
                flag = False
                break
            indexb = indexb + 1 
        if flag == True:
                b.append(a[indexa])
        indexa = indexa + 1
    return b[-1]

print(find_max(a))

#ДЗ: написать для минимума и другой для макса с одним циклом