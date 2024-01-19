class Contact:
    def __init__(self, city, street, number):
        # __ - приватный модификатор доступа
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    # проперти геттер
    @property
    def number(self):
        return self.__number

    # проперти сеттер
    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact_info):
        self.__name = name
        self.__age = age
        if type(contact_info) == Contact:
            self.__contact_info = contact_info
        else:
            raise ValueError('Contact_info must be of data type Contact')
        self.__was_born()

    # приватный метод
    def __was_born(self):
        print(f'Animal {self.__name} was born')

    # метод геттер
    def get_name(self):
        return self.__name

    # метод сеттер
    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if type(value) is not int or value <= 0:
            raise ValueError('Invalid age, it must be positive number')
        else:
            self.__age = value

    def info(self):
        return (f'Name: {self.__name}, Age: {self.__age} '
                f'Birth year: {2024 - self.__age}\n'
                f'Contact info: {self.__contact_info.city}, '
                f'{self.__contact_info.street} {self.__contact_info.number}')

    # полиморфный метод
    def speak(self):
        raise NotImplementedError('speak not implemented')

class Cat(Animal):
    def __init__(self, name, age, contact_info):
        super(Cat, self).__init__(name, age, contact_info)

    def speak(self):
        print('Myau')


class Fish(Animal):
    def __init__(self, name, age, contact_info):
        super(Fish, self).__init__(name, age, contact_info)

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, commands, contact_info):
        super(Dog, self).__init__(name, age, contact_info)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'

    def speak(self):
        print('Gav')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact_info):
        super(FightingDog, self).__init__(name, age, commands, contact_info)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWins: {self.__wins}'

    def speak(self):
        print('Rrrrr gav')


contact_1 = Contact('Bishkek', 'Isanova', 1)

cat = Cat('Tom', 2, contact_1)
cat.set_age(3)
# print(cat.get_age())
# print(cat.info())

dog = Dog('Reks', 5, 'Sit', contact_1)
dog.commands = 'Sit, run'
# print(dog.commands)
# print(dog.info())

# contact_2 = Contact('Osh', 'Lenina', 10)
#         a = b
fightingDog = FightingDog('Snooppy', 1, 'Fight', 10,
                          Contact('Osh', 'Lenina', 10))
# print(fightingDog.info())

# contact_1.number = 15
# print(dog.info())
# print(cat.info())

fish = Fish('Nemo', 8, contact_1)

animal_list = [cat, fish, dog, fightingDog]
for animal in animal_list:
    # применение полиморфизма
    print(animal.info())
    animal.speak()
