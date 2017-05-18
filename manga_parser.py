def parse():
	import json
	import requests 
	from bs4 import BeautifulSoup
	url = "http://manga-sushi.kz/menu/rolls_"
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	rows = soup.select("div.good-item")
	menu = {}
	menu["rolls"] = []
	for item in rows:
		data_id = item['data-id']
		name = item.select("div.good-item-title")[0].text 
		price = item.select("div.good-item-price")[0].text.replace(" ", "")
		desc = item.select("div.good-item-desc div.good-item-in")[0].text
		img = item.select("img.img-responsive")
		q = item.select("span.more")
		num = None
		for i in q:
			num = i["data-rolls_num"]
		images = item.select("img.img-responsive")
		image_url = None
		for i in images:
			image_url = i["src"]
			break
		product = {
			"data_id": data_id, 
			"name": name,
			"description": desc,
			"price": price, 
			"quantity": num, 
			"img_url": image_url
		}
		menu["rolls"].append(product)

	urrl = "http://manga-sushi.kz/menu/sushi"
	t = requests.get(urrl)
	html = t.text
	souup = BeautifulSoup(html, "html.parser")
	roows = souup.select("div.good-item")
	menu["sushi"] = []
	for item in roows:
		data_id = item['data-id']
		name = item.select("div.good-item-title")[0].text
		price = item.select("div.good-item-price")[0].text.replace(" ", "")
		desc = item.select("div.good-item-desc div.good-item-in")[0].text
		img = item.select("img.img-responsive")
		for i in images:
			image = i["src"]
			break
		product = {
			"data_id": data_id, 
			"name": name,
			"description": desc,
			"price": price, 
			"quantity": num, 
			"img_url": image_url
		}
		menu["sushi"].append(product)


	file = open("manga.json", "w", encoding = 'utf-8')
	file.write(json.dumps(menu, ensure_ascii = False))
	file.close()
		

parse()
