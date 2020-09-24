def pow(a, n):
    if n == 1:
        return a
    if n % 2 == 1:
        return pow(a, (int)(n / 2)) * pow(a, (int)(n / 2)) * a
    else:
        return pow(a, (int)(n / 2)) * pow(a, (int)(n / 2))

class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value
        self.accuracy = 0.0000001

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
    def root(self, n):
        left_value = 0
        if self.value>1:
            right_value = self.value
        elif self.value<1:
            right_value = 1
        else:
            self.value = 1
            return self
        length_fractional = 0
        while self.value-pow(left_value, n)>self.accuracy:
            middle_value = (left_value+right_value)/2
            if pow(middle_value, n)>self.value:
                right_value = middle_value
            elif pow(middle_value, n)<self.value:
                left_value = middle_value
            else:
                self.value = middle_value
                return self
        self.value = left_value
        return self

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
    print(Calculator(2).power(1))
    print(Calculator(2).root(2))
