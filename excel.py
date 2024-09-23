from openpyxl import Workbook

def save_to_excel(pala, filename):
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["Nombre", "Sku", "Precio", "Link"])

    for pala in pala:
        sheet.append([pala.name, pala.sku, pala.precio, pala.link])

    workbook.save(filename)