import hashlib
import os
import glob

i = len(glob.glob('.')) #возвращает список путей
listOfChecksums = [] 

# os.walk() обходит дерево каталогов и возвращает генератор кортежей, каждый из которых содержит имя каталога, списки вложенных каталогов и списки имён файлов
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      file = os.path.join(root, name)# соединяет путь со строкой с помощью '/' 
      with open(file, 'rb') as f:
        content = f.read()
      checksum = hashlib.md5(content).hexdigest()
      # hexdigest() позволяет получить зашифрованную строку
      # hashlib.md5() вернёт лишь <md5 HASH object>
      listOfChecksums.append(checksum)


print("Файлы дубликаты:")
for sum in listOfChecksums:
  if listOfChecksums.count(sum) > 1:
    print(sum) 
    