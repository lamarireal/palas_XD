from openpyxl import Workbook

def save_to_excel (names, skus, precios, links, filename):
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["Nombre", "Sku", "Precio", "Link"])

    for name, sku, precio, link in zip(names, skus, precios, links):
        sheet.append([name, sku, precio, link])

    workbook.save(filename)