'''import datetime
var_date_time=datetime.datetime(2022,11,16,hour=21,minute=35,second=34,microsecond=385)
print(f'object datetime-{var_date_time}')
print(f'type-{type(var_date_time)}')

var_date_now=datetime.datetime.now()
print(var_date_now)
print(datetime.datetime.today())
print(datetime.date.today())
a=datetime.date.today()
b=datetime.datetime(int(input('year')),int(input("month")),int(input("day")))'''

'''import datetime
year_of_birgth=datetime.datetime(int(input("year of birgth: ")),int(input("month of birgth: ")),int(input("day of birgth: ")))
current_day=datetime.datetime.now()
how_olr_are_you=current_day-year_of_birgth
print("Your age is: ", how_olr_are_you/365,'years')'''

# colorama модуль призначений для форматування тексту по кольору у терміналі
# виконується за допомогою імпортування та виклику init()

'''from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.BLUE + 'and with a blue background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

from colorama import init
init(autoreset=True)
print(Fore.YELLOW + 'some yellow text')
print('automatically back to default color again')'''




