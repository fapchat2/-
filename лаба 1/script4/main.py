# Напишите скрипт, который разделяет введенный с клавиатуры текст на
# слова и выводит сначала те слова, длина которых превосходит 7
# символов, затем слова размером от 4 до 7 символов, затем – все
# остальные.
text = input('Enter a text: ')

words = text.split()
words.sort(key=len, reverse=True)

flag1, flag2 = 0, 0

for word in words:
  if flag1 == 0 and len(word) > 7:
    print('Слова, длина которых > 7: ', end=' ')
    flag1 += 1
  elif flag2 == 0 and 4 <= len(word) <= 7:
    print('\n Слова, длина которых >=4 <=7: ', end=' ')
    flag2 += 1
  elif (flag1 == 1 or flag2 == 1) and len(word) < 4:
    print('\n Слова, длина которых <4: ', end=' ')
    flag1 += 1
    flag2 += 1

  print(word, end=' ')