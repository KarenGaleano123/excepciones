class Cuenta:
    def __init__(self, saldo, esta_activa):
        self.saldo = saldo
        self.esta_activa = esta_activa

def retirar_dinero(cuenta, cantidad):
    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    if cantidad > cuenta.saldo:
        raise ValueError("Saldo insuficiente")

    cuenta.saldo -= cantidad
    return cuenta.saldo

cuenta = Cuenta(1000, True)

print(retirar_dinero(cuenta, 200))