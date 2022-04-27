import re

checker = False
while checker == False: #пока не введёшь номер из 16 цифр - цикл будет заставлять это делать)
    try:
        money = str(input("Введи номера карты: ")) #Ввод номера карты
        money = re.sub(r'\s', '', money) #удаление пробелов
        money = int(money)
        if len(str(money)) !=16: #Проверка на длину
            raise ValueError
        money = str(money)
        print(money[:4]+' **** **** '+money[12:])
        checker = True
    except ValueError:
        print('ValueError')
   
     
