from random import randint as generate_number, choice
import calculator as cl
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 10))
print(cl.multiplication(8, 4))

my_friend = Person('Jim', 32)
print(my_friend)

cprint('Hello text', 'red', 'on_yellow')
print(emoji.emojize('Python is :thumbs_up:'))

print(config('SECRET_KEY'))
print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
