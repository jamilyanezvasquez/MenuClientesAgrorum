import time
from utility import agregar_cliente, eliminar_cliente, listar_clientes, buscar_cliente
from paises import pais_id


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
            agregar_cliente()
        elif (eleccion == "2"):
            eliminar_cliente()
        elif (eleccion == "3"):
            listar_clientes()
        elif (eleccion == "4"):
            buscar_cliente()
        elif (eleccion == "5"):
            id = input("Ingrese su identificacion: ")
            print("El cliente es de: " + pais_id(id) + "\n")
        elif (eleccion == "6"):
            print("Hasta la proxima!")
            break
        else:
            print("Valor invalido. Porfavor ingrese de nuevo\n")
            time.sleep(3)

if __name__ == "__main__":
    main()