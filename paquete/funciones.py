from paquete.cliente import Cliente
from paquete.producto import Producto

clientes = []
productos = []

class Funciones:
    @staticmethod
    def agregar_cliente():
        nombre = input("\nIngrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        edad = input("Ingrese la edad del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        cliente = Cliente(nombre, email, edad, direccion)
        clientes.append(cliente)
        print(f"\nSe ha agregado al cliente {nombre} al sistema.")

    @staticmethod
    def ver_clientes():
        print("\nLista de clientes:")
        for cliente in clientes:
            print(f"- {cliente}")

    @staticmethod
    def agregar_al_carrito():
        cliente_nombre = input("\nIngrese el nombre del cliente: ")
        producto_nombre = input("Ingrese el nombre del producto: ")
        cliente_encontrado = False
        producto_encontrado = False

        for cliente in clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = True
                for producto in productos:
                    if producto.nombre == producto_nombre:
                        cliente.agregar_al_carrito(producto)
                        producto_encontrado = True
                        break

        if not cliente_encontrado:
            print("\nCliente no encontrado.")
        elif not producto_encontrado:
            print("\nProducto no encontrado.")

    @staticmethod
    def ver_carrito():
        cliente_nombre = input("\nIngrese el nombre del cliente: ")
        cliente_encontrado = False

        for cliente in clientes:
            if cliente.nombre == cliente_nombre:
                cliente_encontrado = True
                cliente.ver_carrito()
                break

        if not cliente_encontrado:
            print("\nCliente no encontrado.")
