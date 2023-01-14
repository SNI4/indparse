#импортируем
import requests
from bs4 import BeautifulSoup

#парсим
def value_parse(first_index, second_index):
	try:
		value = round(float((((BeautifulSoup((requests.get(f'https://www.google.com/finance/quote/{first_index[-3:]}-{second_index}')).text, 'html.parser')).find('div', jscontroller='NdbN0c')).text)[:-36]), 3)
		return (f'{first_index[:-4]} {first_index[-3:]} = {float(first_index[:-4])*value} {second_index}')
	except AttributeError:
		return 'Wrong index!'

#выводим
while True:
	first_index=input('enter first index and amount\n(for example: 1 USD) > ')
	second_index=input('enter second index > ')
	print(value_parse(first_index, second_index))
	ch=input('Restart?(y/n) > ')
	if ch.startswith('y') or ch.startswith('Y'):
		continue
	else:
		break
		