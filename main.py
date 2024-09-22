import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

main_url = "https://www.padelnuestro.com/palas-padel"
params = {
    'product_list_order': 'price_asc', 'p': 1
}

def get_palas_from_page(page_num):
    params['p'] = page_num
    response = requests.get(main_url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    main_products_section = soup.find('ol', class_='products list items product-items')
    if main_products_section:
        palas = main_products_section.find_all('a', class_='product-item-link')
        return [pala['href'] for pala in palas]
    return []

total_pages = 5
all_palas = []
for page in range(1, total_pages + 1):
    palas_on_page = get_palas_from_page(page)
    all_palas.extend(palas_on_page)

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

workbook = Workbook()
sheet = workbook.active

sheet.append(["Nombre", "Sku", "Precio", "Link"])

for name, sku, precio, link in zip(names, skus, precios, links):
    sheet.append([name, sku, precio, link])

workbook.save("palas.xlsx")
