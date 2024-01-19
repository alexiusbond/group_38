class Transport:
    def __init__(self, theModel, theYear, theColor):
        self.model = theModel
        self.year = theYear
        self.color = theColor

    def change_color(self, new_color):
        self.color = new_color
        print('Color changed!')


class Plane(Transport):
    def __init__(self, theModel, theYear, theColor):
        super().__init__(theModel, theYear, theColor)


class Car(Transport):
    # class attribute
    counter = 0
    name = 'FRUNZE'

    # constructor
    def __init__(self, theModel, theYear, theColor, penalties=0):
        # attributes/fields
        super().__init__(theModel, theYear, theColor)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    name = 'BISHKEK'
    counter = 0
    def __init__(self, theModel, theYear, theColor, penalties=0, load_capacity=0):
        super().__init__(theModel, theYear, theColor, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} ({weight} kg) was successfully loaded')


print(f'CARS {Car.name} fabric produced: {Car.counter}')

bmw_car = Car('BMW X7', 2022, 'red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(theYear=2009, penalties=1200, theColor='green', theModel='Honda Civic')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')
# honda_car.color = 'yellow'
honda_car.change_color('yellow')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} NEW COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

bmw_car.drive('Osh')
honda_car.drive('Tokmok')
bmw_car.drive('Batken')


boeing = Plane('Boeing 747', 2023, 'white')
print(f'MODEL: {boeing.model} YEAR: {boeing.year} COLOR: {boeing.color}')
boeing.change_color('blue')
print(f'MODEL: {boeing.model} YEAR: {boeing.year} NEW COLOR: {boeing.color}')

mercedes_truck = Truck('Mercedes 342i', 2000, 'black', 900, 30000)
print(f'MODEL: {mercedes_truck.model} YEAR: {mercedes_truck.year} COLOR: {mercedes_truck.color} '
      f'PENALTIES: {mercedes_truck.penalties} LOAD CAPACITY: {mercedes_truck.load_capacity}')
# mercedes_truck.load_cargo('tomatoes', 45000)
mercedes_truck.load_cargo('apples', 25000)
mercedes_truck.drive('Naryn')


print(f'CARS {Car.name} fabric produced: {Car.counter}')
print(f'TRUCKS {Truck.name} fabric produced: {Truck.counter}')