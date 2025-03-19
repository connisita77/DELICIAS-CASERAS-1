# Panadería Delicias Caseras

Este proyecto consiste en el desarrollo de un sistema de gestión para una panadería que permita el manejo eficiente de productos, pedidos, y sus detalles asociados. El sistema facilitará la administración de productos disponibles (como panes, pasteles, y postres), el registro de pedidos de los clientes y la gestión de los detalles específicos de cada pedido. El objetivo es optimizar el control de inventario, asegurar el manejo correcto de los precios, y mejorar la experiencia del cliente.



## Problema
La panadería "Delicias Caseras" enfrenta desafíos relacionados con la administración de su inventario y la gestión de los pedidos de los clientes. Actualmente, el registro de productos y pedidos se realiza de manera manual, lo que conlleva errores humanos, pérdida de datos y dificultades para dar seguimiento a los detalles de los pedidos. La panadería requiere un sistema digital que centralice la información, permita un control efectivo del inventario y registre cada pedido de manera organizada.



## Tecnologías y Herramientas
Recurso: https://drive.google.com/drive/folders/1sgEohHBFul6AjnAziCO5zaqb4YNQ8BFQ?usp=sharing
GitHub: Para la gestión de versiones del código y colaboración en el desarrollo.


## Características Principales
Gestión de Productos:
Registro de productos de panadería como panes, pasteles, postres, etc.
Almacenamiento de información relevante como nombre del producto, categoría (tipo de pan, pastel, postre), descripción, proveedor, cantidad en stock, precios de venta y de compra.
Gestión de Pedidos:
Creación de nuevos pedidos por parte de los clientes.
Registro de productos dentro de un pedido, incluyendo cantidad, precio por unidad y línea del pedido.
Capacidad para editar y eliminar pedidos.
Inventario Automatizado:
Reducción automática del inventario disponible cuando se registra un pedido.
Control de stock y alertas si un producto está por agotarse.
Consultas y Búsquedas:
Búsqueda de productos por nombre, categoría o código.
Filtrado de pedidos por código de pedido o por producto incluido.
Manejo de Archivos y Persistencia:
Almacenamiento de datos en archivos JSON para garantizar la persistencia de la información entre sesiones.


## Resumen de la Estructura del Sistema
Productos: Diccionario con código de producto, nombre, categoría, proveedor, cantidad en stock y precios.
Pedidos: Diccionario con código de pedido, código del cliente, fecha del pedido y una lista de detalles del pedido.
Detalles de Pedido: Incluye código de producto, cantidad solicitada, precio por unidad y número de línea dentro del pedido.


## Consideraciones Técnicas
Persistencia: Los datos serán almacenados y gestionados mediante archivos JSON.
Modularidad: El sistema se organizará en funciones modulares para la gestión de productos, pedidos, y la manipulación de archivos.
Validación: Se implementarán validaciones para asegurar que los códigos de producto y de pedido sean únicos, así como la verificación del stock disponible antes de procesar un pedido.
