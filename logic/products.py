import json 


def findAll():
    with open("data/products.json", "r" ) as file:
        data = file.read():
        convertListorDict = json.load(data)
        return convertListorDict
def saveAll(data):
    with open("data/products.json", "w", encoding="utf-8" ) as file:
        str(data).encode("utf-8")
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJson)
        return "Se modificó el archivo products.json"

#def updateInventoryByCode(product_code):
    data = findAll()
    for product in data:
        if(product.get("codigo_producto") == product_code):
            quantity = int(input("Ingrese la cantidad de productos que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(f"Se actualizó el {product_code} a {stock}")
            print(saveAll(data))