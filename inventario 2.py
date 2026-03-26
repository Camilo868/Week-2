#The program begins by creating a list where the products will be added.
inventory = []
start = 1

#This is the function where i creatw a dictionary inside a list(in inventory)
def add_product(name,price,quantity,list):
     
    new_product = {
        "Product": name, 
        "price": price,
        "quantity": quantity                              
        }
    list.append(new_product)

#This function only show the registered products. Example: 1.Product: das| price: 13.0| quantity: 2
def Show_product (inventory):
   
    for idx, Show in enumerate(inventory):    
        print(f"{idx+1}.Product: {Show["Product"]}| price: {Show["price"]}| quantity: {Show["quantity"]} ")

# Calculate the total monetary value by multiplying the price by the quantity of each item.
def calcular_tota_prices(inventory):

    total_prices = sum(valor['price']*valor['quantity']for valor in inventory)
    
    return total_prices    

# Add only the physical units available across the entire inventory
def quantity_products(inventory):
    quantity_total = sum(valor['quantity']for valor in inventory)
    return quantity_total

# El ciclo 'while' permite que el programa no se cierre hasta que el usuario elija la opción "4".
while start != 0:
    print("Welcome To My Inventory")
    print("\nPlease select one of the next options you want: ")
    print("1.Add products")
    print("2.Show inventory")
    print("3.Calcular stadistics")
    print("4.Out")

    option=input("Enter an option please: ")

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
            while True:
                
                name_product = input(f"\n Enter the name of the product {product+1}: ")    
                try:
                    price_product = float(input("Enter the price: "))
                    
                    quantity_product = int(input("Enter the quantity: "))
                    # Validation: Avoid empty names and values less than 1
                    if name_product=="":
                        print("Can not be empty") 
                        
                    elif price_product < 1 or quantity_product <1 :
                        print("Enter at least 1")
                    else:
                        break  #If everything its ok out of the loop
                except:
                    print("Enter a value")
            # Call the function to insert the validated product into the list
            add_product(name_product,price_product,quantity_product,inventory)
    #This is the visualization
    elif option == "2":
        
        Show_product(inventory)

    #Here are the math operations
    elif option == "3":
        print("\n Which operation would you like to do?")
        print("1. Total prices")
        print("2. total quantity about products")
        op=input("Enter one of the options: ")
        if op == "1":
            print(f"The total value of the prices is: {calcular_tota_prices(inventory)}")
        elif op =="2":
            print(f"The total quantity of products is: {quantity_products(inventory)}")
        else:
            print("\n Enter one of the options:")
    #Close the program
    elif option == "4":
        print("Good bye")
        start = 0

    else:
        print("Select one  of the options")

