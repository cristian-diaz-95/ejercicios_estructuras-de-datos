inventario = []

def pausar():
    input("\nPresione enter para volver al menú anterior...")

def menu():
    print(        
    "\n________MENÚ_______\n\n",
    "Escoja una opción:\n\n",
    "1. Agregar producto\n",
    "2. Agregar lote de productos\n",
    "3. Eliminar producto del inventario\n",
    "4. Eliminar el producto más reciente\n",
    "5. Ordenar productos alfabéticamente\n",
    "6. Mostrar número total de productos\n",
    "7. Salir\n",
    "\n__________________")
    
while True:
    menu()
    while True:
        opcion = int(input("¿Qué opción desea ejecutar?: "))
        if opcion < 1 or opcion > 7:
            print("ERROR\nOpción ingresada inválida\nVuelve a intentarlo")
            menu()
        else:
            break
            
    match opcion:
        case 1:
            producto = input("\nIngrese el nombre del producto a agregar: ")
            inventario.append(producto) 
            print(f"Producto {producto} agregado exitosamente.")
            pausar()
        case 2:
            while True:
                cantidad = int(input("\n¿Cuántos productos desea agregar en este lote?: "))
                if cantidad <= 0:
                    print("Valor inválido\nVuelve a intentarlo")
                else:
                    break
            for i in range(cantidad):
                prod=input(f"Ingrese el nombre del producto {i+1}: ")
                inventario.append(prod)
            print("Lote de", cantidad, "productos agregado exitosamente.")
            pausar()
        case 3:
            producto_eliminar = input("\nIngrese el nombre del producto a eliminar: ")
            if producto_eliminar in inventario:
                inventario.remove(producto_eliminar)
                print("Producto '", producto_eliminar, "' eliminado del inventario.")
            else:
                print("ERROR: El producto no se encuentra en el inventario.")
            pausar()
        case 4:
            if len(inventario) > 0:
                eliminado = inventario.pop() 
                print("El producto más reciente ('", eliminado, "') ha sido eliminado.")
            else:
                print("ERROR: El inventario está vacío.")
            pausar()
            
        case 5:
            if len(inventario) > 0:
                inventario.sort() 
                print("El inventario ha sido ordenado alfabéticamente.")
            else:
                print("ERROR: El inventario está vacío, no hay nada que ordenar.")
            pausar()
            
        case 6:
            total = len(inventario) 
            print("\nNúmero total de productos en inventario:", total)
            if total > 0:
                print("Lista actual de productos:")
                for p in inventario:
                    print("-", p)
            pausar()
            
        case 7:
            print("\nSaliendo del sistema de inventario... ¡Gracias!\n\n")
            break