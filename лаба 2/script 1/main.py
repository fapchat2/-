# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.

import collections

def take_second(elem):#берёт второй элемент из каждого кортежа, который лежит в списке lst
    return elem[1]

s = open('text.txt').read() # <class 'str'>

#print(filter(lambda x: x.isalpha(), s))# <filter object at 0x7f8c404907c0>

filtered = map(lambda x: x.lower(), filter(lambda x: x.isalpha(), s)) 
#Синтаксис map() с функцией lambda выглядит следующим образом:
# map(lambda item: item[] expression, iterable)
#map() используется для применения функции к каждому элементу итерируемого объекта

#print(collections.Counter(filtered).items()) #dict_items([('н', 3), ('и', 5), ('г', 11), ('а', 4)])
lst = list(map(lambda x: (x[0], x[1]/len(s)), collections.Counter(filtered).items()))
sorted_list = sorted(lst, key=take_second, reverse=True)


for i in range(0, len(sorted_list)):
  print (sorted_list[i][0])