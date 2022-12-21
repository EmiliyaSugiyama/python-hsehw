#1. Найти все числа от 1 до 1000, которые делятся на 17 без остатка # range(1, 1001)
lower = int("1")
upper = int("1001")
n = int("17")
for i in range(lower, upper +1):
    if(i % n ==0):
        print(i, end=' ')


#2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2 # range, str, print("2" in str(102))
print()
print(*(i for i in range(1, 1001) if '2' in str(i)))

#3. Найти все числа от 1 до 10000, которые являются палиндромом # if str(a) == str(a)[::-1]
for a in range(1, 10001):
    if str(a) == str(a)[::-1]:
        print( a, end=" ")

#4.Посчитать количество пробелов в строке # a.count(" "), sum, if chr == ' '
#string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print()
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print(string.count(" "))

print('№8')
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
a = []#1. Найти все числа от 1 до 1000, которые делятся на 17 без остатка # range(1, 1001)
lower = int("1")
upper = int("1001")
n = int("17")
for i in range(lower, upper +1):
    if(i % n ==0):
        print(i, end=' ')


#2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2 # range, str, print("2" in str(102))
print()
print(*(i for i in range(1, 1001) if '2' in str(i)))

#3. Найти все числа от 1 до 10000, которые являются палиндромом # if str(a) == str(a)[::-1]
for a in range(1, 10001):
    if str(a) == str(a)[::-1]:
        print( a, end=" ")

#4.Посчитать количество пробелов в строке # a.count(" "), sum, if chr == ' '
#string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print()
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print(string.count(" "))

#На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
print('№8')
a = []
for i in string:
    if i.isalpha():
        a.append(i.lower())
print(set(a))


#9. На входе список чисел, получить список квадратов этих чисел
print('№9')
print(list(map(lambda x: x ** 2, range(1, 11))))

#10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2.
#На выходе получить словарь из самой точки и расстояния до этой точки из начала координат (0, 0)

print("№10")
coords = [(1, 1), (2, 3), (5, 3)]
result_square_distance = {point: point[0] ** 5 - 2 for point in coords}
print(result_square_distance)

print("№11")
#11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.
a = []
for i in range(2, 28):
    if i%2 == 0:
        a.append(i*i)
print(a)

print("№13")
#13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...] # list(map(..., nums_first, nums_second))


nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]

la = lambda x, y: (x + y, x - y)

print(list(map(la, nums_first, nums_second)))


