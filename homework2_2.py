# First one
class Person:
    def __init__(self, name: str, surname: str, age: int, email: str, university: int):
        self.name = self.string_validation(name)
        self.surname = self.string_validation(surname)
        self.age = self.number_validation(age)
        self.email = self.email_validator(email)
        self.university = self.string_validation(university)

    @staticmethod
    def string_validation(value):
        if value.isdigit():
            raise ValueError("Wrong Value")
        else:
            return value

    @staticmethod
    def number_validation(value):
        if type(value) == str:
            raise ValueError("Wrong Value")
        else:
            return value

    def email_validator(self, email):
        if "@" not in email:
            raise ValueError("Wrong type of email!!")
        return email

    def present(self):
        print(f"Hi, I'm {self.name} {self.surname}, I'm {self.age} years old. Now I'm studying in {self.university}")


student_1 = Person(name='Elizabeth', surname='Mkhitaryan', age=20, email='elizabethmkhitaryan@gmail.com',
                   university='NPUA')
Person.present(student_1)


class Student(Person):
    def __init__(self, name, surname, age, email, university, year):
        super().__init__(name, surname, age, email, university)
        self.graduationyear = year

    def present(self):
        print(f"Welcome {self.name} {self.surname} to the class of {self.graduationyear}")


student_2 = Student(name='Elizabeth', surname='Mkhitaryan', age=20, email='elizabethmkhitaryan@gmail.com',
                    university='NPUA', year=2019)
Student.present(student_2)


# Second one
class Country:
    def __init__(self, name: str, continent: str):
        self.name = self.string_validation(name)
        self.continent = self.string_validation(continent)

    @staticmethod
    def string_validation(value):
        if type(value) != str:
            raise ValueError("Wrong Value")
        else:
            return value


class Brand:
    def __init__(self, brand_name: str, business_start_date: int):
        self.brand_name = brand_name
        self.business_start_date = business_start_date

    def presentation(self):
        print(f'The {self.brand_name} was founded in {self.business_start_date} year.')


class Season:
    def __init__(self, season_name: str, average_temperature: int):
        self.season_name = season_name
        self.average_temperature = average_temperature

    def presentation(self):
        print(f'In {self.season_name} the average temperature is {self.average_temperature}.')


class Product(Country, Brand, Season):
    def __init__(self, product_name: str, type: str, price: int, quantity: int):
        self.product_name = product_name
        self.type = type
        self.price = price
        self.quantity = quantity

    def presentation(self):
        print(
            f'The {self.product_name} is {self.type} of type, the price is {self.price} AMD'
            f' and the rest of product is {self.quantity} item.')

    def discount(self, percent):
        return self.price - ((self.price / 100) * percent)

    def increase(self, count):
        self.new_count = self.quantity + count
        return self.new_count

    def decrease(self, count):
        return self.new_count - count


product_1 = Product(product_name='lego', type='toy', price=11900, quantity=3)
Product.presentation(product_1)
print(Product.discount(product_1, 20))
print(Product.increase(product_1, 20))
print(Product.decrease(product_1, 2))


# Third one
class Hotel:
    def __init__(self, name: str, place: str, rooms_mid: dict, mid_room_price: int, rooms_lux: dict,
                 lux_room_price: int):
        self.name = name
        self.place = place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price

    def presentation(self):
        print(
            f'Welcome to the {self.name} hotel. Our hotel is located at {self.place}. '
            f'We have ordinary and luxury rooms. The price of ordinary room is {self.mid_room_price}, '
            f'this rooms are free {self.rooms_mid}. And the price of luxury room is {self.lux_room_price},'
            f' this rooms are free {self.rooms_lux}')

    def booking(self, key):
        if self.rooms_mid[key] == 'Busy':
            if 'Free' not in self.rooms_mid.values():
                print('Sorry but all rooms are already taken.')
            else:
                print('Sorry but this room is already taken please enter another one with status free.')
        elif key in self.rooms_mid:
            self.rooms_mid.update({key: 'Busy'})
        return self.rooms_mid



    def discount(self, percent):
        return self.mid_room_price - ((self.mid_room_price / 100) * percent)

    def booking_for_lux(self, key):
        if self.rooms_lux[key] == 'Busy':
            print('Sorry but this room is already taken please enter another one with status free.')
        elif key in self.rooms_lux:
            self.rooms_lux.update({key: 'Busy'})
        return self.rooms_lux

    def available_room_check_for_lux(self, booking_for_lux):
        if self.rooms_lux.values() == 'Busy':
            print("Sorry, for now, we haven't any Free room")
        else:
            print("This rooms are Free")

    def discount_for_lux(self, percent):
        return self.lux_room_price - ((self.lux_room_price / 100) * percent)


room_1 = Hotel(name="Alexandr", place='Abovyan Street, Yerevan',
               rooms_mid={"Room1": "Free", "Room2": "Free", "Room3": "Free"}, mid_room_price=50000,
               rooms_lux={"Room1": "Free", "Room2": "Free", "Room3": "Free"}, lux_room_price=120000)
Hotel.presentation(room_1)
#Hotel.available_room_check(room_1)
print(Hotel.booking(room_1, 'Room1'))
print(Hotel.booking(room_1, 'Room2'))
print(Hotel.booking(room_1, 'Room2'))
print(Hotel.discount(room_1, 10))


class Taxi:
    def __init__(self, car_name: str, car_types: str, price_for_trip: int):
        self.car_name = car_name
        self.car_types = car_types
        self.price_for_trip = price_for_trip

    def presentation(self):
        print(
            f"Hi, we have {self.car_name} car. It's a {self.car_types} type of car. The price for this tour will cost {self.price_for_trip}")

    def discount(self, percent):
        return self.price_for_trip - ((self.price_for_trip / 100) * percent)


taxi_1 = Taxi(car_name='Mercedes', car_types="Lux", price_for_trip=70000)
Taxi.presentation(taxi_1)
print(Taxi.discount(taxi_1, 20))


class Tour(Hotel, Taxi):
    def __init__(self, name_of_tour: str, price_lux: int, price_mid: int, car_name: str, car_types: str,
                 price_for_trip: int, name: str, place: str, rooms_mid: dict, mid_room_price: int, rooms_lux: dict,
                 lux_room_price: int):
        self.name_of_tour = name_of_tour
        self.price_lux = price_lux
        self.price_mid = price_mid
        Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
        Taxi.__init__(self, car_name, car_types, price_for_trip)


    def presentation(self):
        print(f'Hello we offer {self.name_of_tour}. We have two options {self.price_lux} and {self.price_mid},'
              f'which includes transport with {self.car_name} company which provides {self.car_types} '
              f'cars and price for it is {self.price_for_trip}. '
              f'We will stay at {self.name} which offers two types of rooms middle {self.mid_room_price} '
              f'and lux {self.lux_room_price}')


global_presentation = Tour(name_of_tour='Geghard tour', price_lux=50000, price_mid=30000, car_name='ride_over',
                           car_types='BMW', price_for_trip=10000, name='Lerane', place="Geghard",
                           rooms_mid={'Room_1': 'Free', 'Room_2': 'Free', 'Room_3': 'Free'},
                           rooms_lux={'Room_1': 'Free', 'Room_2': 'Free', 'Room_3': 'Free'}, mid_room_price=10000,
                           lux_room_price=20000)
Tour.presentation(global_presentation)
