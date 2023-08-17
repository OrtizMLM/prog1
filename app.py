import requests, re
from bs4 import BeautifulSoup as b 

website = "https://dolarhoy.com"
resultado =  requests.get(website)
content = resultado.content
soup = b(content,"html")

linea = soup.find("div", {"class":"venta"},)
casteo = str(linea)
quitar = '<div class="venta"><div class="label">Venta</div><div class="val">'

regex = re.compile(quitar)

prueba = regex.sub('', casteo)

quit = '</div></div>'
regex1 = re.compile(quit)
pruebaf = regex1.sub('', prueba)


sincaste = pruebaf.replace("$","")
valor = int(sincaste)
print(valor)
g = 9


