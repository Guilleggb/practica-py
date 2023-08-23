from paquete.funciones import Funciones

while True:
    print("""
        ********************************
        
        Opciones:
        
        1- Agregar cliente
        2- Ver lista de clientes
        3- Agregar producto al carrito
        4- Ver carrito de cliente
        5- Salir
        
        ********************************
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Funciones.agregar_cliente()
    elif opcion == "2":
        Funciones.ver_clientes()
    elif opcion == "3":
        Funciones.agregar_al_carrito()
    elif opcion == "4":
        Funciones.ver_carrito()
    elif opcion == "5":
        print("Saliendo...")
        break
