import requests 
from bs4 import BeautifulSoup
url = "http://manga-sushi.kz/menu/rolls_"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("div.good-item")
for item in rows:
	data_id = item['data-id']
	name = item.select("div.good-item-title")[0].text
	price = item.select("div.good-item-price")[0].text
	desc = item.select("div.good-item-desc div.good-item-in")[0].text
	print("order_id:", "%s%s" % (data_id,name))
	print("Ингредиенты:", desc)
	print("Цена:", (price).replace(' ', ''))
	img = item.select("img.img-responsive")
	q = item.select("span.more")
	for i in q:
		num = i["data-rolls_num"]
		print("Количество роллов в одном сете: " + num)
		break
	imgages = item.select("img.img-responsive")
	for i in imgages:
		image = i["src"]
		print(image)
		break
	print('\n\n\n\n\n')

urrl = "http://manga-sushi.kz/menu/sushi"
t = requests.get(urrl)
html = t.text
souup = BeautifulSoup(html, "html.parser")
roows = souup.select("div.good-item")
for item in roows:
	data_id = item['data-id']
	name = item.select("div.good-item-title")[0].text
	price = item.select("div.good-item-price")[0].text
	desc = item.select("div.good-item-desc div.good-item-in")[0].text
	print("order_id:", "%s%s" % (data_id,name))
	print("Ингредиенты:", desc)
	print("Цена:", (price).replace(' ', ''))
	print("Количество суши в одном сете: 1")
	for i in imgages:
		image = i["src"]
		print(image)
		break
	print('\n\n\n\n\n')

