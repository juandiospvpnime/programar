def mostrar_productos(lista_productos, mensaje):
    print(mensaje)
    for producto in lista_productos:
        print(f"- {producto}")

def buscar_producto(lista_productos, producto_buscado):
        producto_encontrado =""
        for producto in lista_productos:
            if producto.capitalize() == producto_buscado.capitalize():
                producto_encontrado = producto
                break
        return producto_encontrado

def ejecutar_sistema_compra(lista_productos, carrito):
    confirmacion = "s"
    mensaje_confirmacion = "¿Queres continuar en la tienda?(s/n)"
    
    while(confirmacion == "s"):
        print("\n--- Sistema de compra ---")
        mostrar_productos(lista_productos, "Listado de productos")
        producto_elegido = input("¿Que añadis a tu carrito?\nNombre del producto: ")
        producto_encontrado = buscar_producto(lista_productos, producto_elegido)

        if producto_encontrado != "":
            print(f"Elegiste el producto: {producto_encontrado}")
            carrito.append(producto_encontrado)
            print("el producto ha sido añadido al carrito!")
        else:
            print(f"No se encontro el producto de nombre: {producto_elegido}")


        if len(carrito)==0:
            print(">>El carrito esta vacio<<")
        else:
            mostrar_productos(carrito, "--- Productos actualmente en el carrito ---")

        confirmacion =input(mensaje_confirmacion)
        confirmacion = confirmacion.lower()
        while(confirmacion != "s" and confirmacion != "n" ):
            print("La respuesta es invalida, intente nuevamente")
            confirmacion =input(mensaje_confirmacion)
            confirmacion = confirmacion.lower()

    print("\nHas finalizado tus compras, vamos a nuestra tienda")



def vender_producto(carrito):
    mostrar_productos(carrito, "--- Lista de productos a la venta ---")
   
    producto_elegido = input("¿Qué producto deseas vender?\nNombre del producto: ")
    producto_encontrado = buscar_producto(carrito, producto_elegido)

    if producto_encontrado == "":
        print(f"No se encontró un producto con el nombre {producto_elegido}")
    else:
        carrito.remove(producto_encontrado)
        print(f"¡Has vendido: {producto_encontrado}!")

def ejecutar_sistema_venta(carrito):
    opcion = 0
    while opcion != "3":
        print("\n--- Sistema de venta ---")
        print("1. Ver productos")
        print("2. Vender un producto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            if len(carrito)==0:
                print("No hay propuctos disponibles a la venta")
            else:
                mostrar_productos(carrito," ---Productos disponibles para la venta--- ")
        elif opcion == '2':
            if len(carrito)==0:
                print("No hay propuctos disponibles a la venta")
            else:
                vender_producto(carrito)
        elif opcion == '3':
            print("¡Gracias por haber visitado mi tienda!")
        else:
            print("Opción inválida, intenta de nuevo.")

    print("Has finalizado tus ventas")

def main():
    carrito = []
    productos = ["Tomate","Mayonesa","Llavero","Libro","Cartera","Microondas","Nevera"]
    ejecutar_sistema_compra(productos, carrito)
    ejecutar_sistema_venta(carrito)
    print("Sistema de compra y venta finalizado. Hasta pronto! Ü")

main()