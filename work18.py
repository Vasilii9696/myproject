# task 1
class Human:
    default_name = None
    default_age = None

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'name: {self.name}, age: {self.age}, money: {self.__money}, house: {self.__house}')

    @staticmethod
    def default_info():
        print(f'default name: {Human.default_name}, default age: {Human.default_age}')

    def earn_money(self):
        self.__money += 100

    def make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print(self.name)
        else:
            print(None)

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        self.make_deal(house, price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 4000000)


Human.default_info()
person = Human('Vasilii', 27)
person.earn_money()
person.info()

house = SmallHouse()
person.buy_house(house, 0.1)
person.info()


import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print('Alphabet:', self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return 'Hello my it school'


eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('H'))
print(eng_alphabet.is_en_letter('Я'))
print(EngAlphabet.example())

class Tomato:
    # три стадии созревания томата в виде словаря
    states = {
        1: 'germination phase',
        2: 'growth phase',
        3: 'flowering Phase'
    }
    # метод инит в нутри которого определены два динамических свойства
    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if self._state != self.states[2]: # проверяет не равна ли текущая стадия последней
            current_index = list(self.states.values()).index(self._state) # преобразование в список чтобы получить доступ к индексу и найти его
            self._state = self.states[current_index + 1] # переводит в следующую стадию созревания

    def is_ripe(self):
        return self._state == self.states[2] # проверяет созрел ли томат


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)] # создается список который содержит объекты классы Tomato
        # для каждого индекса создается создается новый Томато с индексом и добавляется в список

    def grow_all(self):
        for tomato in self.tomatoes: # перебирает каждый томат и переводит его в след стадию созревания
           tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes]) # перебериает каждый томат в списке и с помощью метода
    # is_ripe возвращает Тру если помидор созрел, и возвращает тру если все помидоры созрели

    def give_away_all(self):
        self.tomatoes.clear() # очищает список

class Gardener():
    def __init__(self, name):
        self.name = name
        self._plant = None

    def work(self):
        if self._plant: # проверяет наличие объекта класса
            self._plant.grow() # заставляет его работать с помощью метода grow

    def harvest(self):
        if self._plant and self._plant.all_are_ripe(): # если обЪект существует и не равен Ноне и если все томаты дошли
            # до последней стадии созревания то происходит сбор урожая
            print('Сбор урожая')
        else:
            print('!!!!!!')

    @staticmethod
    def knowledge_base(): #статистический метод который выводит справку в консоль
        print('''sssssss
        ssss
        rrrrr
        ggggg
        hhhhh''')

Gardener.knowledge_base()
bush = TomatoBush(3)
gardener = Gardener('Roman')

for x in range(3):
    gardener.work()
    bush.grow_all()

gardener.harvest()

for x in range(3):
    gardener.work()
    bush.grow_all()

gardener.harvest()