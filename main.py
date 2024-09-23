import requests
from bs4 import BeautifulSoup
from palas import get_all_palas
from excel import save_to_excel

all_palas = get_all_palas(total_pages = 5)

names = []
skus = []
precios = []
links = []

for pala_link in all_palas:
    if pala_link:
        url_pala = pala_link
        response = requests.get(url_pala)
        soup = BeautifulSoup(response.content, 'html.parser')

        name_pala = soup.find('span', class_='base')
        if name_pala:
            names.append(name_pala.text.strip())
        else:
            names.append("STFU")
        
        sku_pala = soup.find('span', class_='sku-label')
        if sku_pala:
            skus.append(sku_pala.text.strip())
        else:
            skus.append("STFU")
        
        precio_pala = soup.find('span', class_='price')
        if precio_pala:
            precios.append(precio_pala.text.strip())
        else:
            precios.append("STFU")
        
        links.append(pala_link)

save_to_excel(names, skus, precios, links, filename="palas.xlsx")