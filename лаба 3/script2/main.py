# Напишите классы «Книга» (с обязательными полями: название, автор,
# код), «Библиотека» (с обязательными полями: адрес, номер) и
# корректно свяжите их. Код книги должен назначаться автоматически
# при добавлении книги в библиотеку (используйте для этого
# статический член класса). Если в конструкторе книги указывается в
# параметре пустое название, необходимо сгенерировать исключение
# (например, ValueError). Книга должна реализовывать интерфейс
# Taggable с методом tag(), который создает на основе строки набор тегов
# (разбивает строку на слова и возвращает только те, которые
# начинаются с большой буквы). Например, tag() для книги с названием
# 'War and Peace’ вернет список тегов ['War’, 'Peace’]. Реализуйте классы
# таким образом, чтобы корректно выполнялся следующий код:
# lib = Library(1, ’51 Some str., NY’)
# lib += Book('Leo Tolstoi’, 'War and Peace’)
# lib += Book('Charles Dickens’, 'David Copperfield’)
# for book in lib:u
# # вывод в виде: [1] L.Tolstoi 'War and Peace’
# print(book)
# # вывод в виде: ['War’, 'Peace’]
# print(book.tag())
import random


from abc import ABC, abstractmethod

class Taggable(ABC):
 
    @abstractmethod
    def tag(self, str):
        pass

class Book(Taggable): 
    def __init__(self, author, name, code):
       self.name = name
       self.author = author
       self.code = code

       if not name or not author or not code:
           raise ValueError

    def tag(self, str):
        lst = str.split()
        for word in lst:
            if word != word.upper():
                list.remove(word)
        return lst
        


       
class Library:

   code = 0
   

   def __init__(self, number, adress):
       self.adress = adress
       self.number = number
       self.lstOfBooks = []
       Library.code = random.randint(888, 9999)
              
   def __iadd__(self, other):
       self.lstOfBooks.append(other)
       return self 

# book = Book("qwe", "wqe", "") # Value error!

lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace') 
lib += Book('Charles Dickens', 'David Copperfield')