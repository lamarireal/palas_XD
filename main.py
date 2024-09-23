import requests
from bs4 import BeautifulSoup
from palas import get_all_palas
from excel import save_to_excel

all_palas = get_all_palas(total_pages = 5)

class Pala:
    def __init__(self, name, sku, precio, link):
        self.name = name
        self.sku = sku
        self.precio = precio
        self.link = link

pala_obj = []

for pala_link in all_palas:
    if pala_link:
        url_pala = pala_link
        response = requests.get(url_pala)
        soup = BeautifulSoup(response.content, 'html.parser')

        name_pala = soup.find('span', class_='base')
        name = name_pala.text.strip() if name_pala else "STFU"
        
        sku_pala = soup.find('span', class_='sku-label')
        sku = sku_pala.text.strip() if sku_pala else "STFU"
        
        precio_pala = soup.find('span', class_='price')
        precio = precio_pala.text.strip() if precio_pala else "STFU"
        
        pala_object = Pala(name=name, sku=sku, precio=precio, link=pala_link)
        pala_obj.append(pala_object)

save_to_excel(pala_obj, filename="palas.xlsx")