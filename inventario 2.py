#The program begins by creating a list where the products will be added.
import modulo_servicios as md

inventory = []
start = 1
 

# El ciclo 'while' permite que el programa no se cierre hasta que el usuario elija la opción "4".
while start != 0:
    print("\nWelcome To My Inventory")
    print("\nPlease select one of the next options you want: ")
    print("1.Add products")
    print("2.Show inventory")
    print("3.Calculate stadistics")
    print("4. Search a product")
    print("5. Update a product")
    print("6.Delete a product")
    print("9.Out")

    option=input("Enter an option please: ").strip()
    
    #Add product
    if option == "1":
  
        # Validation to ensure that the number of records is a positive integer
        while True:
            try:
                quantity_to_register=int(input("\n Enter the quantity of products to register: "))
                if quantity_to_register>0:
                    break
                print("Enter at least one product")

            except ValueError:
                print( " Enter a number " )
        # Loop to capture the data for each individual product    
        for product in range(quantity_to_register):
            name_product=""
            while not name_product:
                name_product = input(f"\n Enter the name of the product {product+1}: ").strip().lower()  
                if name_product=="":
                    print("Can not be empty") 
            
            price_product = 0
            while price_product<1:    
                try:
                    price_product = float(input("Enter the price: "))
                    if price_product < 1 :
                        print("Enter at least one")
                except:
                    print("Enter a correct value")
                
            quantity_product=0
            while quantity_product<1:
                try:
                    quantity_product = int(input("Enter the quantity: "))
                    if quantity_product<1:
                        print("Enter at least 1")
                except:
                    print("Enter a value")

        # Call the function to insert the validated product into the list
            md.add_product(name_product,price_product,quantity_product,inventory)
    
    #This is the visualization
    elif option == "2":
        if not inventory:
            print("There is nothing in the inventory")
        else: 
            md.Show_product(inventory)

    #Here are the math operations
    elif option == "3":
        print("\n Which operation would you like to do?")
        print("1. Total prices")
        print("2. total quantity about products")
        print("3. Expensive product")
        print("4. The product with more stock")
        op=input("Enter one of the options: ")
        if not inventory:
            print("There is nothing in the inventory")
        else:
            if op == "1":
                print(f"The total value of the prices is: {md.calcular_tota_prices(inventory)}")
            elif op =="2":
                print(f"The total quantity of products is: {md.quantity_products(inventory)}")
            elif op=="3":
                
                print(f"The more expemnsive product is: {md.expensive_product(inventory)}")
            elif op =="4":
                print(f"The product with more stock is: {md.more_stock(inventory)}")
            else:
                print("\n Enter one of the options:")
    
    #Search product
    elif option == "4":
       if not inventory:
        print("There is nothing in the inventory")
       else: 
            search=input("Ingrese nombre del producto a buscar :")
            encontrado=md.search_product(inventory,search)
            if encontrado:
                print(f"encontrado:{encontrado} ")
            else:
                print("No existe")
    
    #Update a product
    elif option == "5":
        if not inventory:
            print("There is nothing in the inventory")
        else:

            nombre = input("Nombre del producto a actualizar: ").lower()
            
            if md.search_product(inventory, nombre):
                
              
                new_price = 0
                while new_price < 1:
                    try:
                        new_price = float(input("New price: "))
                    except ValueError:
                        print("Error: The price must be a number.")

                new_quantity = 0
                while new_quantity < 1:
                    try:
                        quant = input("New quantity: ")

                        valor = float(quant)
                        if valor.is_integer():
                            new_quantity = int(valor)
                        else:
                            print("Error: The quantity must be an integer.")
                    except ValueError:
                        print("Error: Enter the correct quantity.")

  
                md.update_product(inventory, nombre, new_price, new_quantity)
                print("Updated.")

            else:
                print("The product does not exist.")

    #Delete product
    elif option == "6":
        if not inventory:
            print("There is nothing in the inventory")
        else:
            name = input("Product to delete: ")
        if md.delete_product(inventory, name):
            print("Removed.")
        else:
            print("Error.")

    
 
    #Close the program
    elif option == "9":
        print("Good bye")
        start = 0

    else:
        print("Select one  of the options")

