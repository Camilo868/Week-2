inventario = []
inicio = 1

def agregar_producto(nombre,precio,cantidad,lista):
     
    nuevo_producto = {
        "Producto": nombre, 
        "Precio": precio,
        "Cantidad": cantidad                              
        }
    lista.append(nuevo_producto)

def mostrar_producto (inventario):
    for idx, mostrar in enumerate(inventario):
        
            print(f"{idx+1}.Producto: {mostrar["Producto"]}| Precio: {mostrar["Precio"]}| Cantidad: {mostrar["Cantidad"]} ")
            


while inicio != 0:
    print("Welcome To My Inventory")
    print("Por favor marca una de las siguientes opciones que desees")
    print("1.Agregar productos")
    print("2.Mostrar inventario")
    print("3.Calcular estadisticas")
    print("4.Salir")

    opcion=input("Ingrese una opcion por favor: ")

    if opcion == "1":
        cantidad_a_registrar=int(input("Ingrese la cantidad de productos que va a registrar: "))
        for producto in range(cantidad_a_registrar):
            nombre_producto = input(f"\n Ingrese nombre del producto {producto+1}: ")
            precio_producto = float(input("Ingrese el precio: "))
            cantidad_producto = int(input("Ingrese la cantidad: "))
            agregar_producto(nombre_producto,precio_producto,cantidad_producto,inventario)
    elif opcion == "2":
        
        print(mostrar_producto(inventario))

    elif opcion == "3":
        print("Se harán calculos")

    elif opcion == "4":
        print("Saliendo del programa")
        inicio = 0

    else:
        print("Marca las opciones indicadas")

