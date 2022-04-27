digit = float(input('введите вещественное число: '))
rubles = int(digit)
kopecks = round((digit - rubles) * 100)

print(rubles, 'руб.', kopecks, 'коп.')
