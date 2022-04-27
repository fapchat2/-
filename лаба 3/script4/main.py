from keyring import delete_password
import re

class StringFormatter:
    def delete(self, numb, text):
        return list(filter(lambda x: len(x) >= numb, text.split()))
    def numbersToAsterisks(self, str):        
        str = re.sub(r'\d+', "*", str)        
        return str
    def oneSpaceAmongTheChars(self, str):
        return ' '.join(list(str))
    def sortByLength(self, st):
        lst = st.split()
        return sorted(lst, key=len)
    def sortBylexicographicOrder(self, st):
        words = st.split()
        words.sort()
        return words


# print("Текст без слов, длина которых меньше {}: ".format(2) , StringFormatter().delete(2, "text ww t texttt t"))
# print("Текст со * вместо каждого числа: ",StringFormatter().numbersToAsterisks("ewq 22 qwe2"))
# print("Текст с пробельчиком после каждого символа: ",StringFormatter().oneSpaceAmongTheChars("ewq 22 qwe2"))
# print("Текст с сортировкой по размеру слова: ",StringFormatter().sortByLength("ewq wwwwwww 22 qwe2"))
print("Текст сортировакой слов lexicographicOrder: ",StringFormatter().sortBylexicographicOrder("неггр негр гариолла рогилла Ваня ваня"))