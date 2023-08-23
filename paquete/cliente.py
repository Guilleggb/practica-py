class Cliente:
    def __init__(self, nombre, email, edad, direccion):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.direccion = direccion
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"Producto {producto} agregado al carrito de {self.nombre}.")

    def eliminar_del_carrito(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)
            print(f"Producto {producto} eliminado del carrito de {self.nombre}.")
        else:
            print(f"Producto {producto} no encontrado en el carrito de {self.nombre}.")

    def ver_carrito(self):
        print(f"Carrito de compras de {self.nombre}:")
        for producto in self.carrito:
            print("- ", producto)

    def comprar_carrito(self):
        pass  # Implementar la lógica para realizar la compra y vaciar el carrito

    def __str__(self):
        return self.nombre
