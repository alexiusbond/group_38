from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    DARK_BLUE = '\33[34m'
    YELLOW = '\33[33m'
    GREEN = '\33[32m'


class Drawable:
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f'Playing song - {song}')

    def stop_music(self):
        print(f'Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color
        else:
            raise TypeError('Wrong data type for color')

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return (f'MODEL: {self.__model} YEAR: {self.__year} '
                f'COLOR: {self.__color.value}{self.__color.name}' + '\33[0m')

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    # def __del__(self):
    #     print(f'Car {self.__model} is deleted from memory')


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel_amount(cls, amount):
        cls.__total_fuel_amount += amount

    @classmethod
    def get_fuel_amount(cls):
        return cls.__total_fuel_amount

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using battery')

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)

    # def drive(self):
    #     print(f'Car {self.model} is driving by using fuel or battery')


print(f'Fabric FUEL_CAR has {FuelCar.get_fuel_amount()} litters of fuel')

some_car = Car('Ford Mustang', 2000, Color.RED)
print(some_car)

camry_car = FuelCar('Toyota Camry', 2020,
                    Color.DARK_BLUE, 80)
print(camry_car)

tesla_car = ElectricCar('Tesla Model X', 2023,
                        Color.YELLOW, 25000)
print(tesla_car)

prius_car = HybridCar('Toyota Prius', 2009,
                      Color.GREEN, 70, 15000)
print(prius_car)
prius_car.drive()
print(HybridCar.mro())

number_1 = 10
number_2 = 5
print(number_1 + number_2)
print(camry_car + prius_car)
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Camry is better than Prius: {camry_car > prius_car}')
print(f'Camry is better than Prius: {tesla_car == camry_car}')

# FuelCar.__total_fuel_amount -= 100
FuelCar.buy_fuel_amount(500)
print(f'Fabric FUEL_CAR has {FuelCar.get_fuel_amount()} litters of '
      f'{FuelCar.get_fuel_type()} fuel')

samsung = SmartPhone()

samsung.play_music('Phone music')
camry_car.play_music('Song 1')
prius_car.play_music('Best Song')
camry_car.draw('🚗')
samsung.draw('📱')

if tesla_car.model == 'Tesla Model X':
    print('This car is cool!')

if tesla_car.color == Color.YELLOW:
    print('This car is beautiful')