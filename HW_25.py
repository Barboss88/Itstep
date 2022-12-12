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


import requests
from bs4 import BeautifulSoup    # Був змушений почитати додаткову літературу, в якій описувалася необхідність використання даної бібліотеки та додатковим прописанням 'html.parser', посилаючис
response=requests.get("https://minfin.com.ua/ua/currency/usd/")
response_text=response.text
soup = BeautifulSoup(response_text,'html.parser')
table=soup.find('table',{'class' : "table-response mfm-table mfcur-table-lg mfcur-table-lg-currency-cur has-no-tfoot"})
tr=table.find('td',{'class' : 'mfm-text-nowrap'})
tr=tr.text
tr=tr[:5]
print(f"За банківським  курсом  1 американський доллар = {tr} грн")