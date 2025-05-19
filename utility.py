from cliente import Cliente

clientes = []
def agregar_cliente():
    nombre = input("Ingrese su nombre y apellido: ")
    id = input("Ingrese su identificacion:  ")
    cliente = Cliente(nombre, id)
    clientes.append(cliente)


def eliminar_cliente():
    nombre = input("Ingrese su Nombre y Apellido: ")
    for cliente in clientes:
        if cliente.name == nombre:
            clientes.remove(cliente)
            print("El cliente ha sido eliminado")

def listar_clientes():
    for cliente in clientes:
        print("Nombre: "+ cliente.name +"; Id: "+ cliente.id)

def buscar_cliente():
    nombre = input("Ingrese su Nombre y Apellido: ")
    for cliente in clientes:
        if cliente.name == nombre:
            print("Su identificacion es: " + cliente.id)

