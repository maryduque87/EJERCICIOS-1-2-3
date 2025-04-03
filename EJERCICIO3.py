class Plato:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad
    
    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self.nombre}")
            return False
    
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Stock de {self.nombre} aumentado en {cantidad} unidades. Stock actual: {self.stock}")


class Pedido:
    def __init__(self):
        self.ordenes = {}
    
    def agregar_plato(self, plato, cantidad):
        if plato.verificar_disponibilidad(cantidad):
            self.ordenes[plato.nombre] = self.ordenes.get(plato.nombre, 0) + cantidad
            print(f"{cantidad} unidades de {plato.nombre} agregadas al pedido.")
        else:
            print(f"No se pudo agregar {cantidad} unidades de {plato.nombre} por falta de stock.")
    
    def calcular_total(self, menu):
        total = sum(menu[nombre].precio * cantidad for nombre, cantidad in self.ordenes.items())
        return total
    
    def confirmar_pedido(self, menu):
        for nombre, cantidad in self.ordenes.items():
            if not menu[nombre].vender(cantidad):
                print("El pedido no se pudo completar.")
                return False
        print("Pedido confirmado con éxito.")
        print(f"Total a pagar: ${self.calcular_total(menu)}")
        return True


# para la creacion de los platos
pasta = Plato("Pasta Carbonara", 15, 5)
pizza = Plato("Pizza Margarita", 12, 8)

#platos
menu = {"Pasta Carbonara": pasta, "Pizza Margarita": pizza}

# lo siguiente para la realizacion del pedido
pedido = Pedido()
pedido.agregar_plato(pasta, 3)
pedido.agregar_plato(pizza, 4)
pedido.agregar_plato(pasta, 3)  # en este caso debe de fallar por falta de stock

# re realiza para restablcer y reiniciar
pasta.reabastecer(5)
pedido.agregar_plato(pasta, 3)

# se realiza lo siguiente para confirma el pedido 
pedido.confirmar_pedido(menu)
