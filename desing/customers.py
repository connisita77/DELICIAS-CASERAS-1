
def designClient():
    while True:
        print("""
        **************Menu de Clientes*************
        1. Realizar pedido
        2. Ver pedidos realizados
        3. Salir
        """)
        opc = int(input("Seleccione una opción (1/2/3): "))
        return opc
    
def formularytakeorders():
    dataproducts = findAllproducts()
    dataorders= findAllorders()
    