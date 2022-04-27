# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен.
import os

with open("namesOfSongs.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
#strip() method removes any spaces or specified characters at the start and end of a string
# print(content)



def startRename():
    directory = "songs"
    files=os.listdir(directory)
    i=0 # переменная для цикла
    for file in files:
      os.replace(directory+"/"+file, directory+"/"+content[i][3:]+".mp3")
      #  os.replace() method in Python is used to rename the file or directory
      i+=1

        # os.rename(directory+file, directory+file.replace('.Без названия',''))
startRename()
