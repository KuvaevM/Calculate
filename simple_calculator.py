def pow(a, n):
    if n == 1:
        return a
    if n % 2 == 1:
        return pow(n / 2) * pow(n / 2) * a
    else:
        return pow(n / 2) * pow(n / 2)

class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def power(self, n):
        self.value = self.auxiliary_power(n)
        return  self

    def auxiliary_power(self, n):
        if n == 1:
            return self.value
        if n%2 == 1:
            return self.auxiliary_power((int)(n / 2)) * self.auxiliary_power((int)(n / 2)) * self.value
        else:
            return self.auxiliary_power((int)(n / 2)) * self.auxiliary_power((int)(n / 2))


    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)



if __name__ == '__main__':
    calculator = Calculator(100)
    print(calculator)
    print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(Calculator(100).value + 10)
    print(10 + Calculator(12).value)
    print(Calculator(123).value - Calculator(14).value)
    print(Calculator(14).value / Calculator(2).value)
    print(Calculator(2).power(10))
