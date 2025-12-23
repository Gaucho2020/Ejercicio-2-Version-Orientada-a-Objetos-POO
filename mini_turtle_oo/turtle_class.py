# Creación de la clase tortuga
class Tortuga:
    def __init__(self):                    # Constructor de la clase tortuga
                self.alineacion = 0        # Estado inicial de la tortuga

    def adelante(self, ancho):
        """Mover hacia adelante"""
        print(" " * self.alineacion + " —" * ancho + "┐")
        self.alineacion += ancho * 2

    def abajo(self, alto):
        """Mover hacia abajo"""
        for _ in range(alto):
            print(" " * self.alineacion + "|")
        print(" " * self.alineacion + "🐢")

    def reinicio(self):
        """Reiniciar posición"""
        self.alineacion = 0


