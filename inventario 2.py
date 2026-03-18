inventario = []
inicio = 1

def agregar_producto():
    cantidad_a_registrar=int(input("Ingrese la cantidad de productos que va a registrar: "))
    for producto in range(cantidad_a_registrar):
        nombre_producto = input(f"\n Ingrese nombre del producto {producto+1}: ")
        precio_producto = float(input("Ingrese el precio: "))
        cantidad_producto = int(input("Ingrese la cantidad: "))
        nuevo_producto = {
            "Producto": nombre_producto, 
            "Precio": precio_producto,
            "Cantidad": cantidad_producto                              
            }
        inventario.append(nuevo_producto)


while inicio != 0:
    print("Welcome To My Inventory")
    print("Por favor marca una de las siguientes opciones que desees")
    print("1.Agregar productos")
    print("2.Mostrar inventario")
    print("3.Calcular estadisticas")
    print("4.Salir")

    opcion=input("Ingrese una opcion por favor: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        for idx, mostrar in enumerate(inventario):
        
            print(f"{idx+1}.Producto: {mostrar["Producto"]}| Precio: {mostrar["Precio"]}| Cantidad: {mostrar["Cantidad"]} ")

    elif opcion == "3":
        print("Se harán calculos")

    elif opcion == "4":
        print("Saliendo del programa")
        inicio = 0

    else:
        print("Marca las opciones indicadas")

