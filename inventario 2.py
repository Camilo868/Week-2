

inicio=1
while inicio !=0:
    print("Welcome To My Inventory")
    print("Por favor marca una de las siguientes opciones que desees")
    print("1.Agregar productos")
    print("2.Mostrar inventario")
    print("3.Calcular estadisticas")
    print("4.Salir")

    opcion=input("Ingrese una opcion por favor: ")

    if opcion == "1":
        print("Se agregara un producto")

    elif opcion == "2":
        print("Se mostrará inventario")

    elif opcion == "3":
        print("Se harán calculos")

    elif opcion =="4":
        print("Saliendo del programa")
        break

    else:
        print("Marca las opciones indicadas")

