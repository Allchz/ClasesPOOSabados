class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = valor

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for prod in self.productos:
            if prod.nombre == producto.nombre:
                prod.cantidad += producto.cantidad
                return
        self.productos.append(producto)

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidad = nueva_cantidad
                return
        raise ValueError(f"Producto '{nombre}' no encontrado en el inventario")

    def mostrar_inventario(self):
        if not self.productos:
            return "El inventario está vacío."
        resultado = ""
        for producto in self.productos:
            resultado += str(producto) + "\n"
        return resultado.strip()

    def valor_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.cantidad
        return total


# Pruebas
try:
    # Crear productos
    p1 = Producto("Manzana", 0.5, 10)
    p2 = Producto("Leche", 1.2, 5)
    p3 = Producto("Pan", 0.8, 7)

    # Crear inventario
    inventario = Inventario()

    # Agregar productos
    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)
    inventario.agregar_producto(p3)

    print("Inventario inicial:")
    print(inventario.mostrar_inventario())

    # Actualizar cantidad de un producto
    inventario.actualizar_cantidad("Leche", 10)
    print("\nInventario después de actualizar la cantidad de Leche:")
    print(inventario.mostrar_inventario())

    # Mostrar valor total del inventario
    print(f"\nValor total del inventario: ${inventario.valor_total():.2f}")

except ValueError as e:
    print(f"Error: {e}")

        
        
        
        