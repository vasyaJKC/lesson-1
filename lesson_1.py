#task 1
def clone(lst):
    lst2 = []
    for x in lst:
        lst2.append(x)
    lst2.extend([lst])
    return lst2
#funksiya lst ichidagi malumotlar pustoy list ichiga oxiridan kopy bolib tishadi
print(clone([1,1]))#------->[1, 1, [1, 1]]
print(clone([1, 2, 3]))
print(clone(['x', 'y']))
#-------------------------------------------------------------------------------------------
#task 2
def filter(lst3):
    list = []
    for x in lst3:
        if type(x) == int:
            list.append(x)
    return list
#bu erda type ni tekshirib zaposga tori kesa faqata integer boganini list ga qoshadi
print(filter([1, 2, 3, "a", "b", 4])) #-----> [1,2,3,4]
print(filter([1, "a", "b", 0, 15]))
print(filter([1, 2, "aasf", "1", "123", 123]))
#-------------------------------------------------------------------------------------------
#task 3
def split(nums):
    numbers = nums // 2
    if nums % 2 != 0:
        return [numbers, numbers + 1]
    else:
        return [numbers, numbers]
#soni ikiga bolib cchiqarish kk agar нечетное chislo bosa ong tomoni bita koproq bolishi kk
print(split(4))#--->[2,2]
print(split(10))
print(split(11))
print(split(-9))
#-------------------------------------------------------------------------------------------
#task 4
def jazzify(lst):
    list1 = []
    for x in lst:
        if '7' in x:
            list1.append(x)
        else:
            list1.append(x + '7')
    return list1
print(jazzify(["G", "F", "C"]))#➞ ["G7", "F7", "C7"]
print(jazzify(["Dm", "G", "E", "A"]))
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(jazzify([]))
#------------------------------------------------------------------------------------------

