import requests
from bs4 import BeautifulSoup

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


def get_all_palas(total_pages):
    all_palas = []
    for page in range (1, total_pages + 1):
        palas_on_page = get_palas_from_page(page)
        all_palas.extend(palas_on_page)
    return all_palas