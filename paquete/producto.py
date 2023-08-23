class Producto:
    def __init__(self, nombre, tienda, precio):
        self.nombre = nombre
        self.tienda = tienda
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} en {self.tienda} por ${self.precio}"
        