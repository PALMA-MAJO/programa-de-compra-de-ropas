from abc import ABC, abstractmethod

# Clase abstracta de producto
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass

    def get_precio(self):
        return self.precio

# Clases que heredan de producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_info(self):
        print(f"Camisa: {self.nombre}, Precio: Gs.{self.precio}, Talla: {self.talla}")

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_info(self):
        print(f"Pantalón: {self.nombre}, Precio: Gs.{self.precio}, Talla: {self.talla}")

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_info(self):
        print(f"Zapato: {self.nombre}, Precio: Gs.{self.precio}, Talla: {self.talla}")

# Clase para manejar productos a comprar
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} agregado al carrito.")

    def mostrar_carrito(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            producto.mostrar_info()

    def calcular_total(self):
        total = sum(producto.get_precio() for producto in self.productos)
        print(f"Total a pagar: Gs.{total}")
        return total

# Clase para manejar el inventario
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for i, producto in enumerate(self.inventario, start=1):
            print(f"{i}. ", end="")
            producto.mostrar_info()

    def buscar_producto_por_indice(self, indice):
        if 0 <= indice < len(self.inventario):
            return self.inventario[indice]
        return None

# Inicializar el inventario
tienda = Tienda("Tienda de Ropa")
tienda.agregar_producto(Camisa("Camisa Purpura", 100000, "M"))
tienda.agregar_producto(Pantalon("Pantalón Blanco", 130000, "L"))
tienda.agregar_producto(Zapato("Zapatos de Vestir", 300000, 38))

carrito = Carrito()

def iniciar_compra():
    while True:
        print("\n--- Menú de Compra ---")
        print("1. Ver Inventario")
        print("2. Agregar Producto al Carrito")
        print("3. Ver Carrito")
        print("4. Calcular Total")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tienda.mostrar_inventario()

        elif opcion == "2":
            tienda.mostrar_inventario()
            try:
                seleccion = int(input("Ingresa el número del producto que deseas agregar al carrito: ")) - 1
                producto = tienda.buscar_producto_por_indice(seleccion)
                if producto:
                    carrito.agregar_producto(producto)
                else:
                    print("El producto no ha sido encontrado.")
            except ValueError:
                print("Entrada inválida. Intenta de nuevo por favor.")

        elif opcion == "3":
            carrito.mostrar_carrito()

        elif opcion == "4":
            carrito.calcular_total()

        elif opcion == "5":
            print("Gracias por tu compra. ¡Vuelve prontito!")
            break

        else:
            print("Opción inválida. Intenta de nuevo por favor.")

# Iniciar el programa
iniciar_compra()