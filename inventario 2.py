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

def calcular_tota_precios(inventario):

    total_precios = sum(valor['Precio']*valor['Cantidad']for valor in inventario)
    
    return total_precios    

def cantidad_productos(inventario):
    cantidad_total = sum(valor['Cantidad']for valor in inventario)
    return cantidad_total


while inicio != 0:
    print("Welcome To My Inventory")
    print("\nPor favor marca una de las siguientes opciones que desees")
    print("1.Agregar productos")
    print("2.Mostrar inventario")
    print("3.Calcular estadisticas")
    print("4.Salir")

    opcion=input("Ingrese una opcion por favor: ")

    if opcion == "1":
        while True:
            try:
                cantidad_a_registrar=int(input("\n Ingrese la cantidad de productos que va a registrar: "))
                if cantidad_a_registrar>0:
                    break
                print("Ingrese al menos un producto")

            except ValueError:
                print( " Digite un numero " )
            
        for producto in range(cantidad_a_registrar):
            while True:
                
                nombre_producto = input(f"\n Ingrese nombre del producto {producto+1}: ")    
                try:
                    precio_producto = float(input("Ingrese el precio: "))
                    
                    cantidad_producto = int(input("Ingrese la cantidad: "))
                    if nombre_producto=="":
                        print("NO PUEDE SER VACIO") 
                        
                    elif precio_producto < 1 or cantidad_producto <1 :
                        print("Ingrese al menos 1")
                    else:
                        break
                except:
                    print("Ingrese un valor")
            agregar_producto(nombre_producto,precio_producto,cantidad_producto,inventario)

    elif opcion == "2":
        
        mostrar_producto(inventario)

    elif opcion == "3":
        print("\n Que operacion desea realizar")
        print("1. Total de precios")
        print("2. Cantidad total de productos")
        op=input("Ingrese una de las opciones: ")
        if op == "1":
            print(calcular_tota_precios(inventario))
        elif op =="2":
            print(cantidad_productos(inventario))
        else:
            print("\n ingrese una de las opciones")
    elif opcion == "4":
        print("Saliendo del programa")
        inicio = 0

    else:
        print("Marca las opciones indicadas")

