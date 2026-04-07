def save_csv(inventory, route, add_header=True):
    """
    Save the current inventory to a CSV file.
    """
    # Verify that the inventory is not empty before saving.
    if not inventory:
        print("Error: The inventory is empty. There is no data to save.")
        return

    try:
        # Open (or create) the file in write mode ('w')
        with open(route, 'w', encoding='utf-8') as archivo:
           
            # Write the header if add_header is True
            if add_header:
                archivo.write("name,price,quantity\n")
           
            # Go through the inventory and write down each product
            for product in inventory:
                name = product["Product"]
                price = product["price"]
                quantity = product["quantity"]              
                # We write the row separated by commas with a line break
                archivo.write(f"{name},{price},{quantity}\n")       
        print(f"inventory save in: {route}")

    # Handling specific errors
    except PermissionError:
        print("Error de permisos: No se pudo guardar el archivo. Verifica que no esté abierto en otro programa.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el archivo: {e}")


def charge_csv(route):
    """
    Read and validate the file. Return (product_list, errors).
    """
    loaded = []
    invalid_rows = 0
    try:
        with open(route, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            return None, 0 # File is empty

        header = lines[0].strip().lower()
        if header != "name,price,quantity":
            return "header_error", 0

        for i, line in enumerate(lines[1:], start=2):
            parts = line.strip().split(",")
            
            if len(parts) != 3:
                invalid_rows += 1
                continue

            try:
                name = parts[0].strip().lower()
                price = float(parts[1].strip())
                quantity = int(parts[2].strip())
                
                if not name or price < 0 or quantity < 0:
                    invalid_rows += 1
                    continue
                
                loaded.append({"Product": name, "price": price, "quantity": quantity})
            except ValueError:
                invalid_rows += 1
                continue

        return loaded, invalid_rows

    except FileNotFoundError:
        return None, 0
    except Exception:
        return "error", 0
