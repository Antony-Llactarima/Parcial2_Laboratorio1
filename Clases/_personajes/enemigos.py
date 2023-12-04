class Enemigos:
    def __init__(self, nombre:str, vida:int, velocidad:int, tamanio:list,direccion)->None:
        self.nombre = nombre
        self.vida = vida
        self.velocidad = velocidad
        self.tamanio = tamanio
        self.direccion = direccion
        self.activo = True
        self.ticks_run = 0
        self.tiempo_tick = 0
        self.cambiar_direccion = False
    
    def definir_posicion(self,posicion_ini,posicion):
        self.posicion_inicial = posicion_ini
        self.posicion = posicion
        self.definir_limite()
    
    def definir_limite(self):
        self.limite = [self.posicion[0] + self.tamanio[0], self.posicion[1] + self.tamanio[1]]
    
    def mover_x(self):
        if self.direccion == 'right':
            self.posicion[0] += self.velocidad
        elif self.direccion == 'left':
            self.posicion[0] -= self.velocidad
        self.definir_limite()
    
    def mover_y(self):
        if self.direccion == 'up':
            self.posicion[1] -= self.velocidad
        elif self.direccion == 'down':
            self.posicion[1] += self.velocidad
        self.definir_limite()
    
    def elegir_frame_enemy1(self):
        key_frame = "1"
        if self.ticks_run < 5 and self.direccion == 'right':
            key_frame = "1"
            self.ticks_run += 1
        elif self.ticks_run < 10 and self.direccion == 'right':
            key_frame = "2"
            self.ticks_run += 1
        elif self.ticks_run < 15 and self.direccion == 'right':
            key_frame = "3"
            self.ticks_run += 1
        elif self.ticks_run < 20 and self.direccion == 'right':
            key_frame = "4"
            self.ticks_run += 1
        elif self.ticks_run < 25 and self.direccion == 'right':
            key_frame = "5"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'right':
            key_frame = "6"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        elif self.ticks_run < 5 and self.direccion == 'left':
            key_frame = "7"
            self.ticks_run += 1
        elif self.ticks_run < 10 and self.direccion == 'left':
            key_frame = "8"
            self.ticks_run += 1
        elif self.ticks_run < 15 and self.direccion == 'left':
            key_frame = "9"
            self.ticks_run += 1
        elif self.ticks_run < 20 and self.direccion == 'left':
            key_frame = "10"
            self.ticks_run += 1
        elif self.ticks_run < 25 and self.direccion == 'left':
            key_frame = "11"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'left':
            key_frame = "12"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        return key_frame
    
    def elegir_frame_enemy2(self):
        key_frame = "1"
        if self.ticks_run < 7 and self.direccion == 'up':
            key_frame = "1"
            self.ticks_run += 1
        elif self.ticks_run < 14 and self.direccion == 'up':
            key_frame = "2"
            self.ticks_run += 1
        elif self.ticks_run < 21 and self.direccion == 'up':
            key_frame = "3"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'up':
            key_frame = "4"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        elif self.ticks_run < 7 and self.direccion == 'down':
            key_frame = "6"
            self.ticks_run += 1
        elif self.ticks_run < 14 and self.direccion == 'down':
            key_frame = "7"
            self.ticks_run += 1
        elif self.ticks_run < 21 and self.direccion == 'down':
            key_frame = "8"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'down':
            key_frame = "9"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        return key_frame
    
    def elegir_frame_enemy3(self):
        key_frame = "1"
        if self.ticks_run < 7 and self.direccion == 'right':
            key_frame = "1"
            self.ticks_run += 1
        elif self.ticks_run < 14 and self.direccion == 'right':
            key_frame = "2"
            self.ticks_run += 1
        elif self.ticks_run < 21 and self.direccion == 'right':
            key_frame = "3"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'right':
            key_frame = "4"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        elif self.ticks_run < 7 and self.direccion == 'left':
            key_frame = "6"
            self.ticks_run += 1
        elif self.ticks_run < 14 and self.direccion == 'left':
            key_frame = "7"
            self.ticks_run += 1
        elif self.ticks_run < 21 and self.direccion == 'left':
            key_frame = "8"
            self.ticks_run += 1
        elif self.ticks_run < 30 and self.direccion == 'left':
            key_frame = "9"
            self.ticks_run += 1
            if self.ticks_run >= 30:
                self.ticks_run = 0
        return key_frame
    
    def colision(self,jugador):
        if self.posicion[0] < jugador.limite[0] and self.limite[0] > jugador.posicion[0] and self.posicion[1] < jugador.limite[1] and self.limite[1] > jugador.posicion[1]:
            jugador.vida -= 1
            jugador.posicion = jugador.posicion_inicial