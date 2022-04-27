# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.

password = input('input your password!')
if (len(password) < 8):
  print('your password is very bad!')
elif(len(password) >= 8 and len(password) < 12):
    print('your password is ok!')
elif(len(password) >= 12):
    print('your password is great!')
