import json
import os

INVENTORY_FILE = "inventario.json"


def cargar_inventario():
    """Carga el inventario desde un archivo JSON."""
    if not os.path.exists(INVENTORY_FILE):
        return {}

    with open(INVENTORY_FILE, "r") as archivo:
        return json.load(archivo)


def guardar_inventario(inventario):
    """Guarda el inventario en un archivo JSON."""
    with open(INVENTORY_FILE, "w") as archivo:
        json.dump(inventario, archivo, indent=4)


def mostrar_inventario(inventario):
    print("\n--- INVENTARIO ---")
    if not inventario:
        print("No hay productos registrados.")
    else:
        for producto, datos in inventario.items():
            print(f"{producto} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
    print()


def agregar_producto(inventario):
    producto = input("Nombre del nuevo producto: ").strip().lower()

    if producto in inventario:
        print("Ese producto ya existe en el inventario.\n")
        return

    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad inicial: "))
    except ValueError:
        print("Valores inválidos.\n")
        return

    inventario[producto] = {"precio": precio, "cantidad": cantidad}
    guardar_inventario(inventario)
    print(f"Producto '{producto}' agregado correctamente.\n")


def aumentar_inventario(inventario):
    producto = input("Producto a aumentar: ").strip().lower()

    if producto not in inventario:
        print("Ese producto no está en el inventario.\n")
        return

    try:
        cantidad = int(input("Cantidad a agregar: "))
    except ValueError:
        print("Valor inválido.\n")
        return

    inventario[producto]["cantidad"] += cantidad
    guardar_inventario(inventario)
    print("Inventario actualizado.\n")


def comprar(inventario):
    producto = input("Producto a comprar: ").strip().lower()

    if producto not in inventario:
        print("Ese producto no existe.\n")
        return

    try:
        cantidad = int(input("Cantidad a comprar: "))
    except ValueError:
        print("Valor inválido.\n")
        return

    if cantidad > inventario[producto]["cantidad"]:
        print("No hay suficiente stock.\n")
        return

    total = cantidad * inventario[producto]["precio"]
    inventario[producto]["cantidad"] -= cantidad
    guardar_inventario(inventario)

    print(f"Compra realizada. Total a pagar: ${total:.2f}\n")


def menu():
    inventario = cargar_inventario()

    while True:
        print("=== SISTEMA DE TIENDA ===")
        print("1. Ver inventario")
        print("2. Comprar producto")
        print("3. Agregar producto nuevo")
        print("4. Aumentar inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            comprar(inventario)
        elif opcion == "3":
            agregar_producto(inventario)
        elif opcion == "4":
            aumentar_inventario(inventario)
        elif opcion == "5":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()
