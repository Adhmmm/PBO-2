class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(3, 6)) # Output: 9
print(Kalkulator.subtract(10, 8)) # Output: 2
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(6, 2)) # Output: 12
print(Kalkulator.divide(10, 2)) # Output: 5.0