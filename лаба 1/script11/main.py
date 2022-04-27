# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
# for x in frange(1, 5, '0.1'):
# print(x)
# # выводит
# 1
# 1.1
# 1.2
# 1.3
# 1.4
# ...
# 4.9

import decimal
#Генератор – это языковое средство (объект вокруг функции с инструкцией yield)
def frange(start, stop, step):
  while start < stop:
    yield start
    start += decimal.Decimal(step)

for x in frange(1, 5, '0.1'):
  print(x)