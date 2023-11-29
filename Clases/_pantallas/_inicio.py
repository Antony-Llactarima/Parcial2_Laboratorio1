class Pantallas:
    def __init__(self, nombre, pos_button, limit_boton, activo, primera_vuelta) -> None:
        self.nombre = nombre
        self.pos_button = pos_button
        self.limit_boton = limit_boton
        self.activo = activo
        self.primera_vuelta = primera_vuelta
    
    def mover_boton_x(self, direccion):
        if direccion == "left":
            if self.pos_button - 1 > 0:
                self.pos_button -= 1
        elif direccion == "right":
            if self.pos_button + 1 <= self.limit_boton:
                self.pos_button += 1
    
    def mover_boton_y(self, direccion):
        if direccion == "up":
            if self.nombre == "menu" and self.pos_button - 2 > 0:
                self.pos_button -= 2
            elif self.nombre == "ajuste" and self.pos_button - 1 > 0:
                self.pos_button -= 1
            elif self.nombre == 'wins' and self.pos_button - 1 > 0:
                self.pos_button -= 1
        if direccion == "down":
            if self.nombre == "menu" and self.pos_button + 2 <= self.limit_boton:
                self.pos_button += 2
            elif self.nombre == "ajuste" and self.pos_button + 1 <= self.limit_boton:
                self.pos_button += 1
            elif self.nombre == 'wins' and self.pos_button + 1 <= self.limit_boton:
                self.pos_button += 1
    
    def activar_pantalla(self):
        if self.activo == False:
            self.activo = True
    
    def desactivar_pantalla(self):
        if self.activo:
            self.activo = False
    
    def guardar_ultima_pantalla(self, pantalla_antigua):
        self.pre_pantalla = pantalla_antigua


pantalla_menu = Pantallas('menu', 1, 4, True, 0)
pantalla_game_over = Pantallas('game_over', 1,3, False, 0)
pantalla_wins = Pantallas('wins', 1, 4, False, 0)
pantalla_ajuste = Pantallas('ajuste', 1, 3, False, 0)
pantalla_puntaje = Pantallas('puntaje', 1, 1, False, 0)
pantalla_juego = Pantallas('juego', 1, 2, False, 0)
pantalla_niveles = Pantallas('niveles', 1, 4, False, 0)