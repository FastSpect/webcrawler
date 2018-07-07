import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page=0
	while page <= max_pages:
		url= ("https://proxyfl.info/search/black%20panther/"+str(page)+"/7//")

		source_code = requests.get(url)
		plain_text= source_code.text
		soup= BeautifulSoup(plain_text, "html.parser")
		for link in soup.findAll('a',{'class':'detLink'}):
			href="https://proxyfl.info"+str(link.get('href'))
			title= link.string
			print(title)
			print(href+"\n")	
		page+=1


spider(1)

