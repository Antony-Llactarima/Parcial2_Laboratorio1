class Personaje:
    def __init__(self, nombre:str, vida:int, velocidad:int, tamanio:list)->None:
        self.nombre = nombre
        self.vida = vida
        self.velocidad = velocidad
        self.tamanio = tamanio
        self.direccion = 'right'
        self.moviendose = False
        self.puntaje = 0
        self.ticks_run = 0
        self.tiempo_tick = 0
    
    def activar_gravedad(self, force_gravedad: int, force_salto:int)->None:
        self.force_gravedad = force_gravedad
        self.force_salto = force_salto
        self.saltar = False
        self.time_saltando = 0
        self.gravedad = True
    
    def definir_posicion(self, posicion:list):
        self.posicion_inicial = posicion
        self.posicion = self.posicion_inicial
        
        self.definir_limite()
    
    def definir_limite(self):
        self.limite = [self.posicion[0] + self.tamanio[0], self.posicion[1] + self.tamanio[1]]
    
    def update_posicion(self,list_pos_plat: list, list_lim_plat:list)->None:
        colision_pared = False
        
        if self.saltar == False:
            self.ejercer_gravedad() 
        
        for i in range(len(list_pos_plat)):
            if colision_pared == False:
                colision_pared = self.detectar_paredes(list_pos_plat[i], list_lim_plat[i], self.direccion)
            
            if self.gravedad:
                if self.saltar == False:
                    self.detectar_suelo(list_pos_plat[i], list_lim_plat[i])
                if self.saltar:
                    self.detectar_techo(list_pos_plat[i], list_lim_plat[i])
    
    def detectar_limites(self, tam_screen:tuple)->bool:
        caida_limite = False
        if self.posicion[0] < 0:
            self.posicion[0] = 0
        elif self.limite[0] > tam_screen[0]:
            self.posicion[0] = tam_screen[0] - self.tamanio[0]
        elif self.posicion[1] < 0:
            self.posicion[1] = 0
        elif self.limite[1] > tam_screen[1]:
            caida_limite = True
            self.posicion[1] = tam_screen[1] - self.tamanio[1]
        self.definir_limite()
        return caida_limite
    
    def detectar_suelo(self, pos_suelo:tuple, limit_suelo:tuple)->None:
        if (self.limite[1] >= pos_suelo[1]) and (self.limite[1] <= (pos_suelo[1] + self.force_gravedad)) and (self.posicion[0] < limit_suelo[0]) and (self.limite[0] > pos_suelo[0]):
                self.posicion[1] = pos_suelo[1] - self.tamanio[1]
                self.saltar = True
                self.definir_limite()
    
    def detectar_techo(self, pos_techo:tuple, limit_techo:tuple)->None:
        if self.saltando:
            if (self.posicion[1] < (limit_techo[1])) and (self.posicion[0] < limit_techo[0]) and (self.limite[0] > pos_techo[0]) and (self.posicion[1] >= (limit_techo[1]) - self.velocidad):
                self.posicion[1] = limit_techo[1]
                self.saltar = False
                self.definir_limite()
    
    def detectar_paredes(self, pos_pared:tuple, limit_pared:tuple, direccion:str)->bool:
        colision = False
        if direccion == 'left':
            if (self.posicion[0] < limit_pared[0]) and (self.posicion[1] < limit_pared[1]) and (self.limite[1] > pos_pared[1]) and (self.posicion[0] >= limit_pared[0] - self.velocidad):
                self.posicion[0] = limit_pared[0]
                self.definir_limite()
                colision = True
        elif direccion == 'right':
            if (self.limite[0] > pos_pared[0]) and (self.posicion[1] < limit_pared[1]) and (self.limite[1] > pos_pared[1]) and (self.limite[0] <= pos_pared[0] + self.velocidad):
                self.posicion[0] = pos_pared[0] - self.tamanio[0]
                self.definir_limite()
                colision = True
        return colision
    
    def limitar_pantalla(self, limite_pantalla:list):
        if (self.limite[0] > limite_pantalla[0]):
            self.posicion[0] = limite_pantalla[0] - self.tamanio[0]
        elif (self.posicion[0] < 0):
            self.posicion[0] = 0
        elif (self.posicion[1] < 0):
            self.posicion[1] = 0
        
        self.definir_limite()
    
    def ejercer_gravedad(self):
        self.posicion[1] += self.force_gravedad
        self.definir_limite()
    
    def saltando(self, key_saltar:bool)->None:
        if self.saltar and key_saltar:
            self.posicion[1] -= self.force_salto
            self.definir_limite()
            self.time_saltando += 1
            if self.time_saltando > 10:
                self.saltar = False
                self.time_saltando = 0
        else:
            self.saltar = False
            self.time_saltando = 0
    
    def movimiento_x(self):
        if self.direccion == 'left':
            self.posicion = [self.posicion[0] - self.velocidad, self.posicion[1]]
        elif self.direccion == 'right':
            self.posicion = [self.posicion[0] + self.velocidad, self.posicion[1]]
        
        self.definir_limite()
    
    def bajar_vida(self, danio:int):
        self.vida -= danio
    
    def subir_vida(self, plus:int):
        self.vida += plus

