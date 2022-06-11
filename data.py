from random import choice
import string
from .lib.combinatorics import all_pairs2

# фунция случайной строки из символов и цифр
def GenRandomLine(length=15, chars="LUD"):
    char_set = ''
    if 'L' in chars: char_set += string.ascii_lowercase
    if 'U' in chars: char_set += string.ascii_uppercase
    if 'D' in chars: char_set += string.digits
    if 'P' in chars: char_set += string.punctuation
    if 'R' in chars: char_set += 'абвгдежзийклмнопрстуфхцчшщъыьэюАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ'
    return ''.join([choice(char_set) for i in range(length)])


login = 'cto8@ya.ru'
password = '12345678'
new_password = '11111111'
password_invalid = '00000000'

login_password_valid = [login, password]
login_password_pairs_invalid = list(all_pairs2.all_pairs2([
                ['fake@fakemail.ru', ''],
                ['11111111', '']
                ]))
'''
== email ==
Проверка валидного адреса
Валидный email, содержащий строчный и заглавные буквы
Начинающийся с цифры в локальной части email
Начинающийся с цифры в доменной части email
Email c несколькими точками в локальной и доменной части
Email с дефисом в локальной части email
Email с дефисом в доменной части email
Email с нижним подчёркиванием в локальной части email
Email с нижним подчёркиванием в доменной части email
Длинный Email (локальная часть 64 символа, доменная состоит из 3 участков по 63 символа, разделённых точками)
'''
emails_valid = ['', 'faKe@faKemail.ru', '5fake@fakemail.ru', 'fake@5fakemail.ru', 'fa-ke@fake-mail.ru', 'f.a.k.e@f.a.k.e.mail.ru', 
                f'{GenRandomLine(64)}@{GenRandomLine(63)}.{GenRandomLine(63)}.{GenRandomLine(63)}']
'''
== email ==
Проверка на невалидность 
Пустое поле
Превышение длины локальной части (максимальная допустимая 64 символа)
Превышение длины доменного имени (максимальная допустимая 255 символов)
Превышение длины участка доменного имени между точками (максимальная допустимая 63 символа)
Отсутствие @ в email
Отсутствие локальной части
Отсутствие доменной части
Содержит две точки подряд
Локальная часть начинается с . (точки)
Доменная часть начинается с . (точки)
'''                
emails_invalid = [' ', f'{GenRandomLine(65)}@fakemail.ru', f'faKe@{GenRandomLine(256)}.ru', f'faKe@fakemail.{GenRandomLine(65)}.ru', 
                'faKefaKemail.ru', '@faKemail.ru', 'faKe@', 'faKe@faKemail', 'fa..Ke@faKemail.ru', 
                '.faKe@faKemail.ru', 'faKe@.faKemail.ru']

# ТЗ: пароль содержит маленькие латинские буквы+цифры и состоит из не менее 8 символов
passwords_valid = ['', f'{GenRandomLine(8, "LD")}', f'{GenRandomLine(9, "LD")}', 
                f'{GenRandomLine(254, "LD")}', f'{GenRandomLine(8, "D")}', 
                f'{GenRandomLine(9, "D")}', f'{GenRandomLine(8, "L")}', f'{GenRandomLine(9, "L")}']
passwords_invalid = [' ', f'{GenRandomLine(7, "LD")}', f'{GenRandomLine(3, "LD")}', 
                f'{GenRandomLine(8, "U")}', f'{GenRandomLine(8, "LUP")}', 
                f'{GenRandomLine(16, "R")}']

phones_valid = ['9099099999', '909-909-9999', ' 909 909     9999', '909*909*9999', '+9?0&9*9)0+9*9*9-9/9', '+72345678901', '82345678901' ]
phones_invalid = [' ', f'{GenRandomLine(9, "D")}', f'{GenRandomLine(3, "D")}', 
                f'{GenRandomLine(11, "D")}', f'{GenRandomLine(20, "D")}', 
                f'{GenRandomLine(10, "U")}', f'{GenRandomLine(10, "L")}', 
                f'{GenRandomLine(9, "U")}', f'{GenRandomLine(9, "L")}', 
                f'{GenRandomLine(10, "R")}']

phone_valid = '9236302662'
phone_invalid = '923630266'


     