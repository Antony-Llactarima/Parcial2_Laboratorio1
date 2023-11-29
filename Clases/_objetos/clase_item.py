class Items:
    def __init__(self, nombre, tamanio, posicion):
        self.nombre = nombre
        self.tamanio = tamanio
        self.posicion = posicion
        self.activo = True
        self.time = 0
    
    def colision(self, jugador)->bool:
        colisionismo = False
        if self.activo:
            if jugador.posicion[0] < self.limite[0] and jugador.limite[0] >self.posicion[0] and jugador.posicion[1] < self.limite[1] and jugador.limite[1] > self.posicion[1]:
                self.activo = False
                colisionismo = True
                self.efecto_colision(jugador)
        return colisionismo
    
    def definir_limite(self):
        self.limite = [self.posicion[0] + self.tamanio[0], self.posicion[1] + self.tamanio[1]]
    
    def movimiento(self):
        if self.activo:
            if self.time <= 10:
                self.posicion[1] -= 1
            elif self.time <= 20:
                self.posicion[1] += 1
            else:
                self.time = 0
            self.definir_limite()
    
    def efecto_colision(self, jugador):
        jugador.puntaje += 10

