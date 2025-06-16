"""
cambiar las listas por diccionarios []
cambiar las funciones para que usen diccionarios []
busqueda de diccionarios dentro de istas []
agregar el procesamiento de codigos de productos []

"""

opcion=0
lista_productos=[]
#producto={"nombre":nombre, "cantidad":stock, "precio":precio}

def solicitarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ").lower()
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return [nombreProd, precioProd, stockProd]
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):
    
    for producto in lista_productos:
        if producto["nombre"]==nombre:
            return producto
    
    return None

def guardarProducto(nombre, precio, stock):

    if buscarProducto(nombre)==None:
        producto={
            "nombre":nombre,
            "cantidad": stock,
            "precio":precio}
        lista_productos.append(producto)
    else:
        print("Ya existe un producto con ese nombre")

def actualizarProducto(nombre, nuevoPrecio, nuevoStock):
    productoBuscado=buscarProducto(nombre)
    if productoBuscado!=None:
        indice=lista_productos.index(productoBuscado)
        productoBuscado["precio"]=nuevoPrecio
        productoBuscado["cantidad"]=nuevoStock
        lista_productos[indice]=productoBuscado
        print(f"El producto {nombre} fue actualizado correctamente")
    else:
        print("El producto que intenta actualizar no existe")

def modificarInventarioCompleto():
    if len(lista_productos)==0:
        print("No hay productos")
    else:
        for producto in lista_productos:
            print(f"Nombre: {producto["nombre"]} \t\t Precio: ${producto["precio"]} \t\t Stock: {producto["cantidad"]}")

def eliminarProducto(nombre):
    productoBuscado=buscarProducto(nombre)
    if productoBuscado!=None:
        lista_productos.remove(productoBuscado)
        print("Producto eliminado correctamente")
    else:
        print("No existe un producto con ese nombre")

while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            infoProducto=solicitarProducto()
            if infoProducto!=None:
                guardarProducto(infoProducto[0],
                                infoProducto[1],
                                infoProducto[2])
        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print("-"*60)
                print(f"Nombre: {productoEncontrado["nombre"]} \t\t Precio: ${productoEncontrado["precio"]} \t\t Stock: {productoEncontrado["cantidad"]}")
                print("-"*60)
        case "3":
            infoProducto=solicitarProducto()
            if infoProducto!=None:
                actualizarProducto(infoProducto[0], infoProducto[1], infoProducto[2])
        case "4":
            modificarInventarioCompleto()
        case "5":
            nombre=input("Ingrese el nombre del producto a eliminar: ")
            eliminarProducto(nombre)
        case "6":
            print("Saliendo...")
        case default:
            print("Opción no valida")