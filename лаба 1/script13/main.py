# Напишите собственную версию генератора enumerate под названием
# extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
# print(elem, cum, frac)

# В переменной cum хранится накопленная сумма на момент текущей
# итерации, в переменной frac – доля накопленной суммы от общей
# суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
# вывод будет таким:
# (1, 1, 0.1)
# (3, 4, 0.4)
# (4, 8, 0.8)
# (2, 10, 1)

import decimal

def frange(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

for x in frange(2, 5, '0.1'):
  print(x)

def extra_enumerate(x):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

for i, elem, cum, frac in extra_enumerate(x):
  print(elem, cum, frac)