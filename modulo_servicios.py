inventory = []

def add_product(name, price, quantity, list):
    """
    Agrega un nuevo producto a la lista de inventario.

    Args:
        name (str): Nombre del producto a registrar.
        price (float): Precio unitario del producto.
        quantity (int): Cantidad de unidades disponibles.
        list (list): Lista donde se almacenará el producto.

    Returns:
        None: La función modifica la lista directamente.
    """
    
    # Crea el diccionario con la estructura del producto
    new_product = {
        "Product": name, 
        "price": price,
        "quantity": quantity                               
        }
    
    # Añade el diccionario creado a la lista recibida
    list.append(new_product)


def Show_product (inventory):
    """
    Recorre el inventario para imprimir cada producto con su índice, nombre, precio y cantidad.

    Args:
        inventory (list): Lista de diccionarios que representan los productos.

    Returns:
        None: La función realiza impresiones en pantalla y no devuelve ningún valor.
    """
    
    # Itera sobre la lista obteniendo el índice (comenzando en 0) y el diccionario del producto
    for idx, Show in enumerate(inventory):    
        # Muestra el número de producto (idx+1) seguido de sus atributos clave
        print(f"{idx+1}.Product: {Show["Product"]}| price: {Show["price"]}| quantity: {Show["quantity"]} ")

def calcular_tota_prices(inventory):
    """
    Calcula el valor total monetario de todo el inventario sumando el costo de cada producto.

    Args:
        inventory (list): Lista de diccionarios que contienen los datos de los productos.

    Returns:
        float: La suma total de multiplicar el precio por la cantidad de cada artículo.
    """

    # Realiza la suma de la multiplicación de precio por cantidad de cada elemento en el inventario
    total_prices = sum(valor['price']*valor['quantity']for valor in inventory)    

    # Devuelve el valor final calculado
    return total_prices

def quantity_products( inventory):
    """
    Suma la cantidad total de unidades de todos los productos en el inventario.

    Args:
        inventory (list): Lista de diccionarios que contienen los datos de los productos.

    Returns:
        int: La suma total de las cantidades disponibles de cada artículo.
    """
    
    # Suma el valor de la llave 'quantity' de cada elemento en el inventario
    quantity_total = sum(valor['quantity']for valor in inventory)
    
    # Devuelve el total acumulado de unidades
    return quantity_total

def expensive_product(inventory):
    """
    Busca y determina cuál es el producto con el precio más alto en el inventario.

    Args:
        inventory (list): Lista de diccionarios que representan los productos.

    Returns:
        dict: El diccionario completo del producto que tiene el mayor precio.
    """
    
    # Se toma el primer elemento del inventario como punto de referencia inicial
    expensive=inventory[0]
    
    # Se recorre cada producto para comparar su precio con el del actual más caro
    for product in inventory:
        # Si el precio del producto actual es mayor al guardado, se actualiza la referencia
        if product["price"]>expensive["price"]:
            expensive=product
            
    # Se devuelve el objeto del producto que resultó tener el precio máximo
    return expensive

def more_stock(inventory):
    """
    Identifica el producto que tiene la mayor cantidad de unidades en el inventario.

    Args:
        inventory (list): Lista de diccionarios que contienen la información de los productos.

    Returns:
        dict: El diccionario del producto con el stock más alto.
    """
    
    # Se establece el primer producto como el de mayor stock inicialmente
    stock=inventory[0]
    
    # Se recorre la lista para comparar las cantidades de cada producto
    for product in inventory:
        # Si la cantidad del producto actual supera a la del guardado, se actualiza
        if product["quantity"] > stock["quantity"]:
            stock=product
            
    # Se devuelve el producto que resultó tener más existencias
    return stock

def search_product(inventory, name):
    """
    Busca un producto específico dentro del inventario por su nombre.

    Args:
        inventory (list): Lista de diccionarios que contienen los productos.
        name (str): Nombre del producto que se desea buscar.

    Returns:
        dict: El diccionario del producto si se encuentra coincidencia, de lo contrario devuelve None.
    """
    
    # Recorre cada producto dentro de la lista de inventario
    for product in inventory:

        # Compara el nombre del producto con el nombre buscado en minúsculas
        if product["Product"]== name.lower():

            # Si coinciden, devuelve el objeto del producto encontrado
            return product
        
def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente en el inventario.

    Args:
        inventory (list): Lista de diccionarios que contienen los productos.
        name (str): Nombre del producto que se desea actualizar.
        new_price (float, optional): Nuevo precio a asignar. Por defecto es None.
        new_quantity (int, optional): Nueva cantidad a asignar. Por defecto es None.

    Returns:
        bool: True si el producto fue encontrado y actualizado, False en caso contrario.
    """
    
    # Utiliza la función search_product para localizar el producto por su nombre
    product = search_product(inventory, name)
    
    # Si el producto existe, se procede con la actualización
    if product:
        # Si se proporcionó un nuevo precio, se actualiza en el diccionario
        if new_price is not None: product["price"] = new_price
        
        # Si se proporcionó una nueva cantidad, se actualiza en el diccionario
        if new_quantity is not None: product["quantity"] = new_quantity
        
        # Indica que la operación fue exitosa
        return True
        
    # Indica que el producto no fue encontrado
    return False

def delete_product(inventory, name):
    """
    Elimina un producto del inventario buscando su coincidencia por nombre.

    Args:
        inventory (list): Lista de diccionarios que contienen los productos.
        name (str): Nombre del producto que se desea eliminar.

    Returns:
        bool: True si el producto fue encontrado y eliminado, False en caso contrario.
    """
    
    # Busca el producto en el inventario utilizando la función search_product
    product = search_product(inventory, name)
    
    # Si el producto existe dentro de la lista, procede a borrarlo
    if product:
        # Elimina el diccionario del producto de la lista de inventario
        inventory.remove(product)
        
        # Retorna True para confirmar que la eliminación fue exitosa
        return True
        
    # Retorna False si el producto no se encontró en el inventario
    return False
