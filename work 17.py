# task1

class Example:
    a = 2
    b = 3

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def func1(self):
        self.e = 4
        print(self.e)

    def func_sum(self):
        return self.a + self.b

    def func2(self):
        return self.c ** self.d


exampleObject = Example(7, 8)
print(exampleObject.a)
exampleObject.func1()
print(exampleObject.func2())
print(exampleObject.func_sum())


# task2

class Calculator:
    def __init__(self):
        pass

    def input_numbers(self):
        a = float(input('число 1: '))
        b = float(input('число 2: '))
        return a, b

    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'ощибка деление на ноль'


calculator = Calculator()

number1, number2 = calculator.input_numbers()

print('сумма: ', calculator.sum(number1, number2))
print('разность: ', calculator.difference(number2, number2))
print('умножение:', calculator.multiplication(number1, number2))
print('деление:', calculator.divide(number1, number2))


# Home Work

class String_or_Number:
    def __init__(self):
        pass

    def reading_input(self, a):
        if isinstance(a, str):
            return self.func_string(a)
        elif isinstance(a, int):
            return self.func_number(a)
        else:
            return 'неправильные данные'

    def func_string(self, string):
        vowels = 'aeiouAEIOU'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        len_vowels = [x for x in string if x in vowels]
        num_len_vowels = len(len_vowels)
        len_consonants = [x for x in string if x in consonants]
        num_len_consonants = len(len_consonants)
        res = num_len_vowels * num_len_consonants
        return len_vowels if res <= len(string) else len_consonants


    def func_number(self, number):
        even = sum([int(x) for x in str(number) if int(x) % 2 == 0])
        return even * len(str(number))


str_or_num = String_or_Number()
input_a = input('значение: ')
result = str_or_num.reading_input(input_a)
print(str_or_num.reading_input(input_a))


