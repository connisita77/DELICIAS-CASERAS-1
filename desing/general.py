from desing.customers import *

def menu ():
  print ("""
      ************BIENVENIDO AL MENU***********
        1.registrar el pedido
        2.productos
        3.editar el pedido
        0.salir
        
           """)

  connisita= input("ingrese la opcion deseada: ")
  match connisita:
        case "1":
            while True:
                option = designClient()
                match option:
                    case "1":
                        print(...)
