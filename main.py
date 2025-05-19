import time, utility
def display_menu():
    print("1. Agregar Cliente")
    print("2. Eliminar Cliente")
    print("3. Listar Clientes")
    print("4. Buscar cliente por Nombre")
    print("5. Determinar Pais del Cliente")
    print("6. Salir\n")

def main():

    while True:
        display_menu()
        eleccion = input("Elija una opcion: ")
        if (eleccion == "1"):
            pass
        elif (eleccion == "2"):
            pass
        elif (eleccion == "3"):
            pass
        elif (eleccion == "4"):
            pass
        elif (eleccion == "5"):
            pass
        elif (eleccion == "6"):
            print("Hasta la proxima!")
            break
        else:
            print("Valor invalido. Porfavor ingrese de nuevo\n")
            time.sleep(3)




if __name__ == "__main__":
    main()