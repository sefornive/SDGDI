#Prueba4
entrada = {}

def validar_codigo(codigo):
    if len(codigo) != 6:
        print("El código debe tener 6 caracteres.")
        return False
    letras = sum(1 for c in codigo if c.isalpha() and c.isupper())
    numeros = sum(1 for c in codigo if c.isdigit())
    if letras != 4 or numeros != 2:
        print("El código debe tener al menos 1 letras mayúsculas y 2 números.")
        return False
    return True

def comprar_entrada():
    nombre = input("Ingrese nombre de comprador: ")
    if entrada.get(nombre):
        print("Ese estudiante ya está registrado.")
        return
    
    while True:
        tipoEntrada = input("Ingrese tipo de entrada (G/V): ").upper()
        if validarEntrada(tipoEntrada):
            break
    while True:
        codigo = input("Ingrese código de confirmación: (ej: ABCd12): ").upper()
        if validar_codigo(codigo) and codigo not in entrada:
            break
        elif codigo in entrada:
            print("Código ya registrado.")

    entrada[nombre] = {
        "nombre": nombre,
        "codigo": codigo,
        "tipo": tipoEntrada
    }

    print("Código validado. ¡Entrada registrada con éxito!")

def validarEntrada(tipoEntrada):
    if tipoEntrada.upper() not in ['G', 'V']:
        print("Entrada inválido. Usa 'G' o 'V'.")
        return False
    return True

def consultarComprador(nombre):
    nombre = input("Ingrese nombre de comprador a buscar: ")
    if nombre in entrada:
        print(f"{entrada[nombre]}")
    else:
        print("El comprador no se encuentra.")

def cancelarCompra():
    nombre = input("Ingrese nombre de comprador a cancelar: ").lower()
    if nombre in entrada:
        del entrada[nombre]
        print("¡Compra cancelada!")
    else:
        print("Comprador no encontrado.")

def menu():
    while True:
        print("Menú Principal")
        print("1. Comprar entrada.")
        print("2. Consultar comprador.")
        print("3. Cancelar compra.")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=consultarComprador(nombre)
            if productoEncontrado!=None:
                print(f"Tipo de entrada: {consultarComprador["tipo", [2]]}, Codigo: {consultarComprador["codigo", [3]]}")
        elif opcion == '3':
            cancelarCompra()
        elif opcion == '4':
            print("Programa terminado...")
            break
        else:
            print("Opción inválida.")

menu()