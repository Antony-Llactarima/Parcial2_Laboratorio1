class Niveles:
    def __init__(self, nivel, activo):
        self.nivel = nivel
        self.activo = activo
    
    def activacion(self):
        self.activo = True
    
    def desactivacion(self):
        self.activo = False

nivel_1 = Niveles(1, False)
nivel_2 = Niveles(2, False)
nivel_3 = Niveles(3, False)