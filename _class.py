class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Avanza {pasos} pasos → x = {self.posicion_x}")

    def abajo(self):
        print("Lápiz abajo")

    def reiniciar(self):
        self.posicion_x = 0
        print("Posición reiniciada a 0")
