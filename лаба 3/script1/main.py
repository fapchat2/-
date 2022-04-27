# Дополнить класс таким образом, чтобы выполнялся следующий код:
# frac = Fraction(7, 2)
# print(-frac)
# print(~frac)
# print(frac**2)
# print(float(frac))
# print(int(frac))

# выводит
# выводит
# выводит
# выводит
# выводит
# -7/2
# 2/7
# 49/4
# 3.5
# 3


class Fraction:

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d / %d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)



frac = Fraction(7, 2)

print(frac)