import pygame
from pygame.locals import *
import Clases._pantallas._inicio as screens
import Clases._personajes.class_personajes as prsn
import recursos._plataformas.pos_plataformas as list_nivel
import Clases._ajustes._ajustes as sett
import Clases._niveles.niveles as levels
from _carga_recursos.dicc_imgs import *
from _carga_recursos.dicc_sprites import *
from recursos._items.pos_coins import *
from _carga_recursos._carga_puntaje.carga_puntaje import *
from _carga_recursos._carga_sounds.carga_sound import *
from _carga_recursos._carga_musica._carga_musica import *
from recursos._enemigos.pos_enemigos import *


class Juego:
    # FUNCION CONSTRUCTOR
    def __init__(self):
        self.tam_screen = (1080,720)
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.tam_screen)
        pygame.display.set_caption("Juego Parcial 2")
        self.tick = 0
        
        self.activo()
    
    # FUNCION DONDE ESTA CORRIENDO EL PROGRAMA
    def activo(self):
        fps = 30
        activado = True
        self.play_musica('menu','play')
        while activado:
            self.clock.tick(fps)
            activado = self.manejo_eventos(activado)
            
            if screens.pantalla_juego.activo:
                self.eventos_teclado_juego()
                self.update_jugador()
            
            self.draw_screen()
            if screens.pantalla_menu.activo:
                self.draw_menu()
            elif screens.pantalla_niveles.activo:
                self.draw_selecc_niveles()
            elif screens.pantalla_puntaje.activo:
                self.draw_puntajes()
            elif screens.pantalla_ajuste.activo:
                self.draw_options()
            elif screens.pantalla_juego.activo:
                self.draw_juego()
            elif screens.pantalla_game_over.activo:
                self.draw_game_over()
            elif screens.pantalla_wins.activo:
                self.draw_victoria()
            
            self.update()
            
        self.salir_juego()
    
    # EVENTOS DE PANTALLA
    def manejo_eventos(self, activado:bool):
        for event in pygame.event.get():
            if event.type == QUIT:
                activado = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    activado = self.eventos_menu(event.key)
                    self.eventos_game_over(event.key)
                    self.eventos_selecc_niveles(event.key)
                elif event.key == pygame.K_RIGHT:
                    activado = self.eventos_menu(event.key)
                    self.eventos_game_over(event.key)
                    self.eventos_selecc_niveles(event.key)
                elif event.key == pygame.K_UP:
                    activado = self.eventos_menu(event.key)
                    self.eventos_victoria(event.key)
                    self.eventos_ajustes(event.key)
                elif event.key == pygame.K_DOWN:
                    activado = self.eventos_menu(event.key)
                    self.eventos_victoria(event.key)
                    self.eventos_ajustes(event.key)
                elif event.key == pygame.K_c:
                    activado = self.eventos_menu(event.key)
                    self.eventos_selecc_niveles(event.key)
                    self.eventos_puntajes()
                    self.eventos_victoria(event.key)
                    self.eventos_game_over(event.key)
                    self.eventos_ajustes(event.key)
        return activado
    
    # ZONA DE MENU
    def eventos_menu(self, event):
        juego_activo = True
        if screens.pantalla_menu.activo:
            if event == pygame.K_c:
                self.play_sonidos('click')
                if screens.pantalla_menu.pos_button == 1:
                    screens.pantalla_menu.desactivar_pantalla()
                    screens.pantalla_niveles.activar_pantalla()
                    screens.pantalla_niveles.primera_vuelta = 0
                elif screens.pantalla_menu.pos_button == 2:
                    screens.pantalla_menu.desactivar_pantalla()
                    screens.pantalla_puntaje.guardar_ultima_pantalla('menu')
                    screens.pantalla_puntaje.primera_vuelta = 0
                    screens.pantalla_puntaje.activar_pantalla()
                elif screens.pantalla_menu.pos_button == 3:
                    screens.pantalla_menu.desactivar_pantalla()
                    screens.pantalla_ajuste.activar_pantalla()
                    screens.pantalla_ajuste.guardar_ultima_pantalla("menu")
                    screens.pantalla_ajuste.primera_vuelta = 0
                    screens.pantalla_ajuste.limit_boton = 3
                elif screens.pantalla_menu.pos_button == 4:
                    juego_activo = False
            else:
                self.play_sonidos('btn')
                if event == pygame.K_LEFT:
                    screens.pantalla_menu.mover_boton_x("left")
                elif event == pygame.K_RIGHT:
                    screens.pantalla_menu.mover_boton_x("right")
                elif event == pygame.K_UP:
                    screens.pantalla_menu.mover_boton_y("up")
                elif event == pygame.K_DOWN:
                    screens.pantalla_menu.mover_boton_y("down")
        return juego_activo
    
    # ZONA DE EL SELECCIONADOR DE NIVELES
    def eventos_selecc_niveles(self, event):
        if screens.pantalla_niveles.activo:
            if screens.pantalla_niveles.primera_vuelta == 0:
                screens.pantalla_niveles.primera_vuelta += 1
            else:
                if event == pygame.K_c:
                    self.play_sonidos('click')
                    if screens.pantalla_niveles.pos_button < 4:
                        self.play_musica('menu','stop')
                        screens.pantalla_niveles.desactivar_pantalla()
                        screens.pantalla_juego.activar_pantalla()
                        self.activar_nivel(screens.pantalla_niveles.pos_button)
                    else:
                        screens.pantalla_niveles.desactivar_pantalla()
                        screens.pantalla_menu.activar_pantalla()
                    screens.pantalla_niveles.pos_button = 1
                else:
                    self.play_sonidos('btn')
                    if event == pygame.K_LEFT:
                        screens.pantalla_niveles.mover_boton_x("left")
                    elif event == pygame.K_RIGHT:
                        screens.pantalla_niveles.mover_boton_x("right")
    
    # ZONA DE EVENTOS DE LA PANTALLA DE PUNTAJES
    def eventos_puntajes(self):
        if screens.pantalla_puntaje.activo:
            if screens.pantalla_puntaje.primera_vuelta == 0:
                screens.pantalla_puntaje.primera_vuelta += 1
            else:
                self.play_sonidos('click')
                if screens.pantalla_puntaje.pre_pantalla == 'menu':
                    screens.pantalla_menu.activar_pantalla()
                elif screens.pantalla_puntaje.pre_pantalla == 'victoria':
                    screens.pantalla_wins.activar_pantalla()
                    screens.pantalla_wins.primera_vuelta = 0
                elif screens.pantalla_puntaje.pre_pantalla == 'game_over':
                    screens.pantalla_game_over.activar_pantalla()
                    screens.pantalla_game_over.primera_vuelta = 0
                screens.pantalla_puntaje.desactivar_pantalla()
    
    # ZONA DE EVENTOS DE LA PANTALLA DE AJUSTE
    def eventos_ajustes(self, event):
        if screens.pantalla_ajuste.activo:
            if screens.pantalla_ajuste.primera_vuelta == 0:
                screens.pantalla_ajuste.primera_vuelta += 1
            else:
                if event == pygame.K_UP:
                    self.play_sonidos('btn')
                    screens.pantalla_ajuste.mover_boton_y("up")
                elif event == pygame.K_DOWN:
                    self.play_sonidos('btn')
                    screens.pantalla_ajuste.mover_boton_y("down")
                elif event == pygame.K_c:
                    self.play_sonidos('click')
                    self.ajuste_menu()
                    self.ajuste_juego()
    # AJUSTE INGRESADO DESDE EL MENU
    def ajuste_menu(self):
        if screens.pantalla_ajuste.pre_pantalla == 'menu':
            if screens.pantalla_ajuste.pos_button == 1:
                sett.ajustes.on_off_musica()
                if sett.ajustes.musica == False:
                    self.play_musica('menu','stop')
                else:
                    self.play_musica('menu','play')
            elif screens.pantalla_ajuste.pos_button == 2:
                sett.ajustes.on_off_effectos()
            elif screens.pantalla_ajuste.pos_button == 3:
                screens.pantalla_ajuste.desactivar_pantalla()
                screens.pantalla_menu.activar_pantalla()
                screens.pantalla_ajuste.pos_button = 1
                screens.pantalla_ajuste.primera_vuelta = 0
    # AJUSTE INGRESADO DESDE EL JUEGO
    def ajuste_juego(self):
        if screens.pantalla_ajuste.pre_pantalla == 'juego':
            if screens.pantalla_ajuste.pos_button == 1:
                screens.pantalla_ajuste.desactivar_pantalla()
                screens.pantalla_juego.activar_pantalla()
                self.play_musica('menu','stop')
                self.play_musica('juego','play')
                screens.pantalla_ajuste.pos_button = 1
            elif screens.pantalla_ajuste.pos_button == 2:
                screens.pantalla_ajuste.desactivar_pantalla()
                screens.pantalla_niveles.activar_pantalla()
                self.desactivar_niveles()
                screens.pantalla_ajuste.pos_button = 1
                screens.pantalla_niveles.primera_vuelta = 1
            elif screens.pantalla_ajuste.pos_button == 3:
                sett.ajustes.on_off_musica()
                if sett.ajustes.musica == False:
                    self.play_musica('menu','stop')
                else:
                    self.play_musica('menu','play')
            elif screens.pantalla_ajuste.pos_button == 4:
                sett.ajustes.on_off_effectos()
            elif screens.pantalla_ajuste.pos_button == 5:
                screens.pantalla_ajuste.desactivar_pantalla()
                screens.pantalla_menu.activar_pantalla()
                screens.pantalla_ajuste.pos_button = 1
                self.desactivar_niveles()
    
    # ZONA DE EVENTOS DE LA PANTALLA DE VICTORIA
    def eventos_victoria(self,event):
        if screens.pantalla_wins.activo:
            if screens.pantalla_wins.primera_vuelta == 0:
                screens.pantalla_wins.primera_vuelta += 1
            else:
                if event == pygame.K_UP:
                    self.play_sonidos('btn')
                    screens.pantalla_wins.mover_boton_y('up')
                elif event == pygame.K_DOWN:
                    self.play_sonidos('btn')
                    screens.pantalla_wins.mover_boton_y('down')
                elif event == pygame.K_c:
                    self.play_sonidos('click')
                    if screens.pantalla_wins.pos_button == 1:
                        if levels.nivel_1.activo:
                            self.desactivar_niveles()
                            screens.pantalla_wins.desactivar_pantalla()
                            screens.pantalla_juego.activar_pantalla()
                            self.activar_nivel(2)
                        elif levels.nivel_2.activo:
                            screens.pantalla_wins.desactivar_pantalla()
                            self.desactivar_niveles()
                            self.activar_nivel(3)
                            screens.pantalla_juego.activar_pantalla()
                    elif screens.pantalla_wins.pos_button == 2:
                        self.desactivar_niveles()
                        screens.pantalla_wins.desactivar_pantalla()
                        screens.pantalla_niveles.activar_pantalla()
                        screens.pantalla_niveles.primera_vuelta = 1
                    elif screens.pantalla_wins.pos_button == 3:
                        screens.pantalla_wins.desactivar_pantalla()
                        screens.pantalla_puntaje.activar_pantalla()
                        screens.pantalla_puntaje.guardar_ultima_pantalla('victoria')
                        screens.pantalla_puntaje.primera_vuelta = 1
                    elif screens.pantalla_wins.pos_button == 4:
                        self.desactivar_niveles()
                        screens.pantalla_wins.desactivar_pantalla()
                        screens.pantalla_menu.activar_pantalla()
                    screens.pantalla_wins.pos_button = 1
    
    # ZONA DE EVENTOS DE LA PANTALLA DE GAME OVER
    def eventos_game_over(self, event):
        if screens.pantalla_game_over.activo:
            if screens.pantalla_game_over.primera_vuelta == 0:
                screens.pantalla_game_over.primera_vuelta += 1
            else:
                if event == pygame.K_LEFT:
                    self.play_sonidos('btn')
                    screens.pantalla_game_over.mover_boton_x("left")
                elif event == pygame.K_RIGHT:
                    self.play_sonidos('btn')
                    screens.pantalla_game_over.mover_boton_x("right")
                elif event == pygame.K_c:
                    self.play_sonidos('click')
                    if screens.pantalla_game_over.pos_button == 1:
                        screens.pantalla_game_over.desactivar_pantalla()
                        screens.pantalla_niveles.activar_pantalla()
                        screens.pantalla_niveles.primera_vuelta = 1
                        self.desactivar_niveles()
                    elif screens.pantalla_game_over.pos_button == 2:
                        screens.pantalla_puntaje.guardar_ultima_pantalla("game_over")
                        screens.pantalla_game_over.desactivar_pantalla()
                        screens.pantalla_puntaje.activar_pantalla()
                        screens.pantalla_puntaje.primera_vuelta = 1
                        # self.desactivar_niveles()
                    elif screens.pantalla_game_over.pos_button == 3:
                        screens.pantalla_game_over.desactivar_pantalla()
                        screens.pantalla_menu.activar_pantalla()
                        screens.pantalla_game_over.pos_button = 1
                        self.desactivar_niveles()
    
    # ACTIVADOR DE NIVELES
    def activar_nivel(self, nivel):
        self.declarar_jugador()
        self.play_musica('juego','play')
        if nivel == 1:
            levels.nivel_1.activacion()
        elif nivel == 2:
            levels.nivel_2.activacion()
        elif nivel == 3:
            levels.nivel_3.activacion()
        self.posicionar_jugador()
        self.jugador.activar_gravedad(12,10)
    
    # DECLARACION DEL JUEGADOR SEGUN EL NIVEL ELEGIDO
    def declarar_jugador(self):
        self.jugador = prsn.Personaje("Jugador",3,8,[24,48])
    
    # POSICIONAR AL JUGADOR EN SU POSICION DE INICIO DE CADA NIVEL
    def posicionar_jugador(self):
        if levels.nivel_1.activo:
            posicion = [100, 600]
        elif levels.nivel_2.activo:
            posicion = [900,600]
        else:
            posicion = [528,500]
        self.jugador.definir_posicion(posicion)
    
    # DETECCION DE TECLADO MIENTRAS SE ESTE JUGANDO
    def eventos_teclado_juego(self):
        key_saltar = False
        key_touch = pygame.key.get_pressed()
        self.jugador.moviendose = False
        if key_touch[pygame.K_c]:
            key_saltar = True
        if key_touch[pygame.K_SPACE]:
            screens.pantalla_juego.desactivar_pantalla()
            screens.pantalla_ajuste.activar_pantalla()
            screens.pantalla_ajuste.pre_pantalla = 'juego'
            screens.pantalla_ajuste.primera_vuelta = 1
            screens.pantalla_ajuste.limit_boton = 5
            self.play_musica('juego','stop')
            self.play_musica('menu','play')
        if key_touch[pygame.K_LEFT]:
            self.jugador.direccion = 'left'
            self.jugador.moviendose = True
            self.jugador.movimiento_x()
        if key_touch[pygame.K_RIGHT]:
            self.jugador.moviendose = True
            self.jugador.direccion = 'right'
            self.jugador.movimiento_x()
        if key_saltar:
            self.play_sonidos('salto')
        self.jugador.saltando(key_saltar)
    
    # ZONA DE ACTUALIZACION DEL JUGADOR
    def update_jugador(self)->None:
        colisionismo = False
        if levels.nivel_1.activo:
            self.jugador.update_posicion(list_nivel.lista_pos1, list_nivel.lista_limit1)
            for i in range(len(list_coins_nivel1)):
                colisionismo = list_coins_nivel1[i].colision(self.jugador)
                if colisionismo:
                    self.play_sonidos('coins')
            for i in range(len(list_enemy_1_1)):
                if list_enemy_1_1[i].activo:
                    vida_old = self.jugador.vida
                    list_enemy_1_1[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
        elif levels.nivel_2.activo:
            self.jugador.update_posicion(list_nivel.lista_pos2, list_nivel.lista_limit2)
            for i in range(len(list_enemy_1_2)):
                if list_enemy_1_2[i].activo:
                    vida_old = self.jugador.vida
                    list_enemy_1_2[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
            for i in range(len(list_coins_nivel2)):
                colisionismo = list_coins_nivel2[i].colision(self.jugador)
                if colisionismo:
                    self.play_sonidos('coins')
        elif levels.nivel_3.activo:
            self.jugador.update_posicion(list_nivel.lista_pos3, list_nivel.lista_limit3)
            for i in range(len(list_coins_nivel3)):
                colisionismo = list_coins_nivel3[i].colision(self.jugador)
                if colisionismo:
                    self.play_sonidos('coins')
        
        self.jugador.ticks_run += 1
        if self.jugador.ticks_run % 30 == 0:
            self.jugador.tiempo_tick += 1
            if self.jugador.tiempo_tick > 60:
                screens.pantalla_wins.activar_pantalla()
                screens.pantalla_wins.primera_vuelta = 1
                screens.pantalla_wins.pos_button = 1
                self.jugador.puntaje = self.jugador.puntaje + (60 - self.jugador.tiempo_tick) * 5
                self.jugador.puntaje += self.jugador.vida * 5
                if levels.nivel_1.activo:
                    update_puntajes(self.jugador.puntaje,1)
                elif levels.nivel_2.activo:
                    update_puntajes(self.jugador.puntaje,2)
                elif levels.nivel_3.activo:
                    update_puntajes(self.jugador.puntaje,3)
                self.play_musica('juego','stop')
                self.play_musica('menu','play')
        
        caida = self.jugador.detectar_limites(self.tam_screen)
        if caida:
            self.jugador.bajar_vida(1)
            self.play_sonidos('caida')
            self.posicionar_jugador()
        if self.jugador.vida <= 0:
            screens.pantalla_juego.desactivar_pantalla()
            screens.pantalla_game_over.activar_pantalla()
            screens.pantalla_game_over.primera_vuelta = 1
            screens.pantalla_game_over.pos_button = 1
            self.jugador.puntaje = self.jugador.puntaje + (60 - self.jugador.tiempo_tick) * 5
            self.jugador.puntaje += self.jugador.vida * 5
            if levels.nivel_1.activo:
                update_puntajes(self.jugador.puntaje,1)
            elif levels.nivel_2.activo:
                update_puntajes(self.jugador.puntaje,2)
            elif levels.nivel_3.activo:
                update_puntajes(self.jugador.puntaje,3)
            self.play_musica('juego','stop')
            self.play_musica('menu','play')
    
    # DESACTIVAR NIVELES
    def desactivar_niveles(self):
        levels.nivel_1.desactivacion()
        levels.nivel_2.desactivacion()
        levels.nivel_3.desactivacion()
        self.restaurar_coins(list_coins_nivel1)
        self.restaurar_coins(list_coins_nivel2)
        self.restaurar_coins(list_coins_nivel3)
    
    def restaurar_coins(self, list_coins):
        for i in range(len(list_coins)):
            if list_coins[i].activo:
                pass
            else:
                list_coins[i].activo = True
    
    # ZONA DE DIBUJOS DE LA PANTALLA
    def draw_screen(self):
        self.screen.fill((0,0,0))
    
    # ZONA DE DIBUJO DEL MENU
    def draw_menu(self):
        # FONDO DEL MENU ----------------------------------------------------------
        self.screen.blit(fondos['menu'], (0,0))
        self.screen.blit(img_extras['titulo'],(190,0))
        self.screen.blit(dicc_enemy_3['1'],(0,0))
        # BOTONES ------------------------------------------------
        if screens.pantalla_menu.pos_button == 1:
            self.screen.blit(b_RaB_large['play'],(self.tam_screen[0] / 2 - 300, self.tam_screen[1] / 2 + 100))
        else:
            self.screen.blit(b_WaB_large['play'],(self.tam_screen[0] / 2 - 300, self.tam_screen[1] / 2 + 100))
        
        if screens.pantalla_menu.pos_button == 2:
            self.screen.blit(b_RaB_large['resume'],(self.tam_screen[0] / 2 + 100, self.tam_screen[1] / 2 + 100))
        else:
            self.screen.blit(b_WaB_large['resume'],(self.tam_screen[0] / 2 + 100, self.tam_screen[1] / 2 + 100))
        
        if screens.pantalla_menu.pos_button == 3:
            self.screen.blit(b_RaB_large['ajuste'],(self.tam_screen[0] / 2 - 300, self.tam_screen[1] / 2 + 200))
        else:
            self.screen.blit(b_WaB_large['ajuste'],(self.tam_screen[0] / 2 - 300, self.tam_screen[1] / 2 + 200))
        
        if screens.pantalla_menu.pos_button == 4:
            self.screen.blit(b_RaB_large['exit'],(self.tam_screen[0] / 2 + 100, self.tam_screen[1] / 2 + 200))
        else:
            self.screen.blit(b_WaB_large['exit'],(self.tam_screen[0] / 2 + 100, self.tam_screen[1] / 2 + 200))
    
    # ZONA DE DIBUJO DE LOS PUNTAJES
    def draw_puntajes(self):
        pos_y = 0
        fuente = pygame.font.SysFont('Sans serif',45)
        self.screen.blit(fondos['options'],(0,0))
        pygame.draw.rect(self.screen,(255,255,255),((300,0),(400,720)))
        max_puntajes = mostrar_puntaje()
        for i in range(len(max_puntajes)):
            for j in range(5):
                if j + 1 == 1:
                    nivel_str = fuente.render(f"MAX PUNTAJES DE NIVEL {i + 1}",0,(0,0,0))
                    self.screen.blit(nivel_str, (300,pos_y))
                    pos_y += 35
                    puntaje = fuente.render(f"1: {max_puntajes[i]['1']}",0,(0,0,0))
                elif j + 1 == 2:
                    puntaje = fuente.render(f"2: {max_puntajes[i]['2']}",0,(0,0,0))
                elif j + 1 == 3:
                    puntaje = fuente.render(f"3: {max_puntajes[i]['3']}",0,(0,0,0))
                elif j + 1 == 4:
                    puntaje = fuente.render(f"4: {max_puntajes[i]['4']}",0,(0,0,0))
                elif j + 1 == 5:
                    puntaje = fuente.render(f"5: {max_puntajes[i]['5']}",0,(0,0,0))
                self.screen.blit(puntaje, (510,pos_y))
                pos_y += 35
        self.screen.blit(b_RaB_large['back'], (415,620))
    
    # ZONA DE DIBUJO DE LA PANTALLA DE GAME OVER
    def draw_game_over(self):
        # FONDO DE PANTALLA DE GAME OVER
        self.screen.blit(fondos['game_over'], (0,0))
        self.screen.blit(img_extras['game_over'], (240,0))
        # BOTONES DE LA PANTALLA DE GAME OVER
        if screens.pantalla_game_over.pos_button == 1:
            self.screen.blit(b_RaB_large['newGame'],(80, 500))
        else:
            self.screen.blit(b_WaB_large['newGame'],(80, 500))
        
        if screens.pantalla_game_over.pos_button == 2:
            self.screen.blit(b_RaB_large['resume'], (440,500))
        else:
            self.screen.blit(b_WaB_large['resume'], (440,500))
        
        if screens.pantalla_game_over.pos_button == 3:
            self.screen.blit(b_RaB_large['menu'],(800,500))
        else:
            self.screen.blit(b_WaB_large['menu'],(800,500))
        # PUNTAJE LOGRADO
        fuente = pygame.font.SysFont('Sans serif',60)
        puntaje_total = fuente.render(f"Puntaje Alcanzado:{self.jugador.puntaje}",0,(0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),((300,300),(500,100)))
        self.screen.blit(puntaje_total,(300,300))
    
    # ZONA DE DIBUJO DE LA PANTALLA DE VICTORIA
    def draw_victoria(self):
        # FONDO DE LA PANTALLA DE VICTORIA
        self.screen.blit(fondos['victoria'], (0,0))
        # BOTONES PARA LA PANTALLA DE VICTORIA
        if screens.pantalla_wins.pos_button == 1:
            self.screen.blit(b_RaB_large['continue'],(415,300))
        else:
            self.screen.blit(b_WaB_large['continue'],(415,300))
        if screens.pantalla_wins.pos_button == 2:
            self.screen.blit(b_RaB_large['newGame'],(415,400))
        else:
            self.screen.blit(b_WaB_large['newGame'],(415,400))
        if screens.pantalla_wins.pos_button == 3:
            self.screen.blit(b_RaB_large['resume'],(415,500))
        else:
            self.screen.blit(b_WaB_large['resume'],(415,500))
        if screens.pantalla_wins.pos_button == 4:
            self.screen.blit(b_RaB_large['menu'],(415,600))
        else:
            self.screen.blit(b_WaB_large['menu'],(415,600))
        
        fuente = pygame.font.SysFont('Sans serif',60)
        puntaje_total = fuente.render(f"Puntaje Alcanzado:{self.jugador.puntaje}",0,(0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),((300,50),(500,100)))
        self.screen.blit(puntaje_total,(300,100))
    
    # ZONA DE DIBUJO AJUSTE 
    def draw_options(self):
        # FONDO DE PANTALLA DE OPCIONES --------------------------------------
        self.screen.blit(fondos['options'], (0,0))
        # BOTONES DE OPCIONES ----------------------------------
        if screens.pantalla_ajuste.pre_pantalla == 'menu':
            self.draw_ajuste_menu()
        elif screens.pantalla_ajuste.pre_pantalla == 'juego':
            self.draw_ajuste_juego()
    # AJUSTE DE DIBUJO DE AJUSTE DESDE EL MENU
    def draw_ajuste_menu(self):
        if screens.pantalla_ajuste.pos_button == 1:
            self.screen.blit(b_RaB_cortos['music'],(440,300))
            if sett.ajustes.musica:
                self.screen.blit(b_RaB_cortos['check'],(540, 300))
            else:
                self.screen.blit(b_RaB_cortos['cross'],(540, 300))
        else:
            self.screen.blit(b_WaB_cortos['music'],(440,300))
            if sett.ajustes.musica:
                self.screen.blit(b_WaB_cortos['check'],(540, 300))
            else:
                self.screen.blit(b_WaB_cortos['cross'],(540, 300))
        
        if screens.pantalla_ajuste.pos_button == 2:
            self.screen.blit(b_RaB_cortos['sound'],(440, 400))
            if sett.ajustes.efectos_sonidos:
                self.screen.blit(b_RaB_cortos['check'],(540, 400))
            else:
                self.screen.blit(b_RaB_cortos['cross'],(540, 400))
        else:
            self.screen.blit(b_WaB_cortos['sound'],(440, 400))
            if sett.ajustes.efectos_sonidos:
                self.screen.blit(b_WaB_cortos['check'],(540, 400))
            else:
                self.screen.blit(b_WaB_cortos['cross'],(540, 400))
        
        if screens.pantalla_ajuste.pos_button == 3:
            self.screen.blit(b_RaB_large['back'], (415, 500))
        else:
            self.screen.blit(b_WaB_large['back'], (415, 500))
    # AJUSTE DE DIBUJO DE AJUSTE DESDE EL JUEGO
    def draw_ajuste_juego(self):
        if screens.pantalla_ajuste.pos_button == 1:
            self.screen.blit(b_RaB_large['continue'],(415,200))
        else:
            self.screen.blit(b_WaB_large['continue'],(415,200))
        
        if screens.pantalla_ajuste.pos_button == 2:
            self.screen.blit(b_RaB_large['newGame'],(415,300))
        else:
            self.screen.blit(b_WaB_large['newGame'],(415,300))
        
        if screens.pantalla_ajuste.pos_button == 3:
            self.screen.blit(b_RaB_cortos['music'],(440,400))
            if sett.ajustes.musica:
                self.screen.blit(b_RaB_cortos['check'],(540, 400))
            else:
                self.screen.blit(b_RaB_cortos['cross'],(540, 400))
        else:
            self.screen.blit(b_WaB_cortos['music'],(440,400))
            if sett.ajustes.musica:
                self.screen.blit(b_WaB_cortos['check'],(540, 400))
            else:
                self.screen.blit(b_WaB_cortos['cross'],(540, 400))
        
        if screens.pantalla_ajuste.pos_button == 4:
            self.screen.blit(b_RaB_cortos['sound'],(440, 500))
            if sett.ajustes.efectos_sonidos:
                self.screen.blit(b_RaB_cortos['check'],(540, 500))
            else:
                self.screen.blit(b_RaB_cortos['cross'],(540, 500))
        else:
            self.screen.blit(b_WaB_cortos['sound'],(440, 500))
            if sett.ajustes.efectos_sonidos:
                self.screen.blit(b_WaB_cortos['check'],(540, 500))
            else:
                self.screen.blit(b_WaB_cortos['cross'],(540, 500))
        
        if screens.pantalla_ajuste.pos_button == 5:
            self.screen.blit(b_RaB_large['menu'],(415,600))
        else:
            self.screen.blit(b_WaB_large['menu'],(415,600))
    
    # AJUSTE DE DIBUJO DE SELECTOR DE NIVELES
    def draw_selecc_niveles(self):
        fuente = pygame.font.SysFont("Sans-serif",80)
        text_nivel1 = fuente.render("Nivel 1",0,(0,0,0))
        text_nivel2 = fuente.render("Nivel 2",0,(0,0,0))
        text_nivel3 = fuente.render("Nivel 3",0,(0,0,0))
        
        
        # FONDO PARA EL SELECCIONADOR DE NIVELES
        self.screen.blit(fondos['selecc_nivel'], (0,0))
        # SELECCIONAR MENU
        if screens.pantalla_niveles.pos_button == 1:
            pygame.draw.rect(self.screen, (255,0,0), ((56,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_1'],(66,220))
            self.screen.blit(text_nivel1,(66,420))
        else:
            pygame.draw.rect(self.screen, (255,255,255), ((56,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_1'],(66,220))
            self.screen.blit(text_nivel1,(66,420))
        
        if screens.pantalla_niveles.pos_button == 2:
            pygame.draw.rect(self.screen, (255,0,0), ((312,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_2'],(322,220))
            self.screen.blit(text_nivel2,(322,420))
        else:
            pygame.draw.rect(self.screen, (255,255,255), ((312,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_2'],(322,220))
            self.screen.blit(text_nivel2,(322,420))
        
        if screens.pantalla_niveles.pos_button == 3:
            pygame.draw.rect(self.screen, (255,0,0), ((568,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_3'],(578,220))
            self.screen.blit(text_nivel3,(578,420))
        else:
            pygame.draw.rect(self.screen, (255,255,255), ((568,200), (200,300)))
            self.screen.blit(img_selec_nivel['nivel_3'],(578,220))
            self.screen.blit(text_nivel3,(578,420))
        
        if screens.pantalla_niveles.pos_button == 4:
            self.screen.blit(b_RaB_large['menu'],(820,300))
        else:
            self.screen.blit(b_WaB_large['menu'],(820,300))
    
    # DIBUJAR LOS ENEMIGOS DE LOS NIVELES   
    def draw_enemigos(self):
        if levels.nivel_1.activo:
            for i in range(len(list_enemy_1_1)):
                if list_enemy_1_1[i].activo:
                    key = list_enemy_1_1[i].elegir_frame_enemy1()
                    self.screen.blit(dicc_enemy_1[key],list_enemy_1_1[i].posicion)
                    if i == 0:
                        self.update_enemigo(list_enemy_1_1[i],2,0)
                    elif i == 1:
                        self.update_enemigo(list_enemy_1_1[i],6,0)
                    elif i == 2:
                        self.update_enemigo(list_enemy_1_1[i],7,0)
        elif levels.nivel_2.activo:
            for i in range(len(list_enemy_1_2)):
                if list_enemy_1_2[i].activo:
                    key = list_enemy_1_2[i].elegir_frame_enemy1()
                    self.screen.blit(dicc_enemy_1[key],list_enemy_1_2[i].posicion)
                    if i == 0:
                        self.update_enemigo(list_enemy_1_2[i],14,0)
                    elif i == 1:
                        self.update_enemigo(list_enemy_1_2[i],13,0)
            for i in range(len(list_enemy_2_2)):
                if list_enemy_2_2[i].activo:
                    key = list_enemy_2_2[i].elegir_frame_enemy2()
                    self.screen.blit(dicc_enemy_2[key],list_enemy_2_2[i].posicion)
                    list_enemy_2_2[i].mover_y()
                    if list_enemy_2_2[i].limite[1] < list_enemy_2_2[i].posicion_inicial[1] - 100:
                        list_enemy_2_2[i].direccion = "down"
                    elif list_enemy_2_2[i].limite[1] > self.tam_screen[1]:
                        list_enemy_2_2[i].direccion = "up"
                    vida_old = self.jugador.vida
                    list_enemy_2_2[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
            for i in range(len(list_enemy_3_2)):
                if list_enemy_3_2[i].activo:
                    key = list_enemy_3_2[i].elegir_frame_enemy3()
                    self.screen.blit(dicc_enemy_3[key],list_enemy_3_2[i].posicion)
                    self.update_enemigo(list_enemy_3_2[i],6,0)
                    vida_old = self.jugador.vida
                    list_enemy_3_2[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
        elif levels.nivel_3.activo:
            for i in range(len(list_enemy_1_3)):
                if list_enemy_1_3[i].activo:
                    key = list_enemy_1_3[i].elegir_frame_enemy1()
                    self.screen.blit(dicc_enemy_1[key],list_enemy_1_3[i].posicion)
                    if i == 0:
                        self.update_enemigo(list_enemy_1_3[i],11,0)
                    elif i == 1:
                        self.update_enemigo(list_enemy_1_3[i],12,0)
                    vida_old = self.jugador.vida
                    list_enemy_1_3[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
            
            for i in range(len(list_enemy_2_3)):
                if list_enemy_2_3[i].activo:
                    key = list_enemy_2_3[i].elegir_frame_enemy2()
                    self.screen.blit(dicc_enemy_2[key],list_enemy_2_3[i].posicion)
                    list_enemy_2_3[i].mover_y()
                    if list_enemy_2_3[i].limite[1] < list_enemy_2_3[i].posicion_inicial[1] - 100:
                        list_enemy_2_3[i].direccion = "down"
                    elif list_enemy_2_3[i].limite[1] > self.tam_screen[1]:
                        list_enemy_2_3[i].direccion = "up"
                    vida_old = self.jugador.vida
                    list_enemy_2_3[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
            
            for i in range(len(list_enemy_3_3)):
                if list_enemy_3_3[i].activo:
                    key = list_enemy_3_3[i].elegir_frame_enemy3()
                    self.screen.blit(dicc_enemy_3[key],list_enemy_3_3[i].posicion)
                    if i == 0:
                        self.update_enemigo(list_enemy_3_3[i],9,1)
                    elif i == 1:
                        self.update_enemigo(list_enemy_3_3[i],9,2)
                    vida_old = self.jugador.vida
                    list_enemy_3_3[i].colision(self.jugador)
                    vida_new = self.jugador.vida
                    if vida_old != vida_new:
                        self.play_sonidos('golpe')
    
    def update_enemigo(self,enemigo,pos_plataforma,e_3):
        if levels.nivel_1.activo:
            if enemigo.limite[0] < list_nivel.lista_limit1[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                enemigo.direccion = 'right'
            else:
                enemigo.cambiar_direccion = True
            if enemigo.posicion[0] > list_nivel.lista_pos1[pos_plataforma][0] and enemigo.cambiar_direccion == True:
                enemigo.direccion = 'left'
            else:
                enemigo.cambiar_direccion = False
            enemigo.mover_x()
        elif levels.nivel_2.activo:
            if enemigo.nombre == "1":
                if enemigo.limite[0] < list_nivel.lista_limit2[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                    enemigo.direccion = 'right'
                else:
                    enemigo.cambiar_direccion = True
                if enemigo.posicion[0] > list_nivel.lista_pos2[pos_plataforma][0] and enemigo.cambiar_direccion == True:
                    enemigo.direccion = 'left'
                else:
                    enemigo.cambiar_direccion = False
                enemigo.mover_x()
            else:
                if enemigo.limite[0] < list_nivel.lista_limit2[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                    enemigo.direccion = 'right'
                else:
                    enemigo.cambiar_direccion = True
                if enemigo.posicion[0] > list_nivel.lista_pos2[pos_plataforma][0] and enemigo.cambiar_direccion == True:
                    enemigo.direccion = 'left'
                else:
                    enemigo.cambiar_direccion = False
                enemigo.mover_x()
        elif levels.nivel_3.activo:
            if enemigo.nombre == "1":
                if enemigo.limite[0] < list_nivel.lista_limit3[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                    enemigo.direccion = 'right'
                else:
                    enemigo.cambiar_direccion = True
                if enemigo.posicion[0] > list_nivel.lista_pos3[pos_plataforma][0] and enemigo.cambiar_direccion == True:
                    enemigo.direccion = 'left'
                else:
                    enemigo.cambiar_direccion = False
                enemigo.mover_x()
            elif e_3 == 1:
                if enemigo.limite[0] < list_nivel.lista_pos2[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                    enemigo.direccion = 'right'
                else:
                    enemigo.cambiar_direccion = True
                if enemigo.posicion[0] > list_nivel.lista_pos3[pos_plataforma][0] and enemigo.cambiar_direccion == True:
                    enemigo.direccion = 'left'
                else:
                    enemigo.cambiar_direccion = False
                enemigo.mover_x()
            elif e_3 == 2:
                if enemigo.limite[0] < list_nivel.lista_limit3[pos_plataforma][0] and enemigo.cambiar_direccion == False:
                    enemigo.direccion = 'right'
                else:
                    enemigo.cambiar_direccion = True
                if enemigo.posicion[0] > 552 and enemigo.cambiar_direccion == True:
                    enemigo.direccion = 'left'
                else:
                    enemigo.cambiar_direccion = False
                enemigo.mover_x()
    
    # PEGAR LOS SPRITES EN PANTALLA MIENTRAS SE JUEGA
    def draw_juego(self):
        if levels.nivel_1.activo:
            self.screen.blit(fondos_niveles['nivel_1'],(0,0))
            # PLATAFORMAS DEL NIVEL 1-------------------------------------
            self.pegar_plataformas(list_nivel.lista_pos1,dicc_plat['plat'],list_nivel.lista_tam1)
            self.pegar_items(list_coins_nivel1,dicc_coins['1'])
            self.draw_enemigos()
        elif levels.nivel_2.activo:
            self.screen.blit(fondos_niveles['nivel_2'],(0,0))
            # PLATAFORMAS DEL NIVEL 2-------------------------------------
            self.pegar_plataformas(list_nivel.lista_pos2,dicc_plat['plat'],list_nivel.lista_tam2)
            self.draw_enemigos()
            self.pegar_items(list_coins_nivel2,dicc_coins['1'])
        elif levels.nivel_3.activo:
            self.screen.blit(fondos_niveles['nivel_3'],(0,0))
            # PLATAFORMAS DEL NIVEL 3-------------------------------------
            self.draw_enemigos()
            self.pegar_plataformas(list_nivel.lista_pos3,dicc_plat['plat'],list_nivel.lista_tam3)
            self.pegar_items(list_coins_nivel3,dicc_coins['1'])
        
        # Corazones de vidad
        if self.jugador.vida == 3:
            self.screen.blit(dicc_vida['vida'],(0,0))
            self.screen.blit(dicc_vida['vida'],(60,0))
            self.screen.blit(dicc_vida['vida'],(120,0))
        elif self.jugador.vida == 2:
            self.screen.blit(dicc_vida['vida'],(0,0))
            self.screen.blit(dicc_vida['vida'],(60,0))
        elif self.jugador.vida == 1:
            self.screen.blit(dicc_vida['vida'],(0,0))
        
        # JUGADOR PRINCIPAL--------------------------------
        pygame.draw.rect(self.screen, (0,0,0), (self.jugador.posicion, self.jugador.tamanio))
        pos_sprite = [self.jugador.posicion[0] - 12, self.jugador.posicion[1]]
        if self.tick < 5:
            self.tick += 1
            if self.jugador.saltar:
                if self.jugador.moviendose and self.jugador.direccion == 'right':
                    self.screen.blit(dino_move['1_r'],(pos_sprite))
                elif self.jugador.moviendose and self.jugador.direccion == 'left':
                    self.screen.blit(dino_move['1_l'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'right':
                    self.screen.blit(dino_stop['1_r'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'left':
                    self.screen.blit(dino_stop['1_l'],(pos_sprite))
            else:
                if self.jugador.direccion == 'right':
                    self.screen.blit(dino_cae['r'],(pos_sprite))
                elif self.jugador.direccion == 'left':
                    self.screen.blit(dino_cae['l'],(pos_sprite))
            
        elif self.tick < 10:
            self.tick += 1
            if self.jugador.saltar:
                if self.jugador.moviendose and self.jugador.direccion == 'right':
                    self.screen.blit(dino_move['2_r'],(pos_sprite))
                elif self.jugador.moviendose and self.jugador.direccion == 'left':
                    self.screen.blit(dino_move['2_l'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'right':
                    self.screen.blit(dino_stop['2_r'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'left':
                    self.screen.blit(dino_stop['2_l'],(pos_sprite))
            else:
                if self.jugador.direccion == 'right':
                    self.screen.blit(dino_cae['r'],(pos_sprite))
                elif self.jugador.direccion == 'left':
                    self.screen.blit(dino_cae['l'],(pos_sprite))
        elif self.tick < 15:
            self.tick += 1
            if self.jugador.saltar:
                if self.jugador.moviendose and self.jugador.direccion == 'right':
                    self.screen.blit(dino_move['3_r'],(pos_sprite))
                elif self.jugador.moviendose and self.jugador.direccion == 'left':
                    self.screen.blit(dino_move['3_l'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'right':
                    self.screen.blit(dino_stop['3_r'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'left':
                    self.screen.blit(dino_stop['3_l'],(pos_sprite))
            else:
                if self.jugador.direccion == 'right':
                    self.screen.blit(dino_cae['r'],(pos_sprite))
                elif self.jugador.direccion == 'left':
                    self.screen.blit(dino_cae['l'],(pos_sprite))
        elif self.tick <20:
            self.tick += 1
            if self.jugador.saltar:
                if self.jugador.moviendose and self.jugador.direccion == 'right':
                    self.screen.blit(dino_move['4_r'],(pos_sprite))
                elif self.jugador.moviendose and self.jugador.direccion == 'left':
                    self.screen.blit(dino_move['4_l'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'right':
                    self.screen.blit(dino_stop['4_r'],(pos_sprite))
                elif self.jugador.moviendose == False and self.jugador.direccion == 'left':
                    self.screen.blit(dino_stop['4_l'],(pos_sprite))
            else:
                if self.jugador.direccion == 'right':
                    self.screen.blit(dino_cae['r'],(pos_sprite))
                elif self.jugador.direccion == 'left':
                    self.screen.blit(dino_cae['l'],(pos_sprite))
            if self.tick >= 20:
                self.tick = 0
        fuente = pygame.font.SysFont("Sans-serif",60)
        tiempo = fuente.render(f"Tiempo:{self.jugador.tiempo_tick}//60",0,(255,255,255))
        self.screen.blit(tiempo,(800,0))
        
        puntaje = fuente.render(f"Puntos:{self.jugador.puntaje}",0,(255,255,255))
        self.screen.blit(puntaje,(400,0))
    
    # PEGAR LOS ITEMS
    def pegar_items(self,lista_items,img_item):
        cat_desactivado = 0
        for i in range(len(lista_items)):
            if lista_items[i].activo:
                lista_items[i].time += 1
                lista_items[i].movimiento()
                self.screen.blit(img_item,(lista_items[i].posicion))
            else:
                cat_desactivado += 1
        if cat_desactivado == len(lista_items):
            screens.pantalla_juego.desactivar_pantalla()
            screens.pantalla_wins.activar_pantalla()
            screens.pantalla_wins.primera_vuelta = 1
            screens.pantalla_wins.pos_button = 1
            self.jugador.puntaje = self.jugador.puntaje + (60 - self.jugador.tiempo_tick) * 10
            self.jugador.puntaje += self.jugador.vida * 10
            if levels.nivel_1.activo:
                update_puntajes(self.jugador.puntaje,1)
            elif levels.nivel_2.activo:
                update_puntajes(self.jugador.puntaje,2)
            elif levels.nivel_3.activo:
                update_puntajes(self.jugador.puntaje,3)
            self.play_musica('juego','stop')
            self.play_musica('menu','play')
    
    # PEGAR LOS SPRITES DE LAS PLATAFORMAS
    def pegar_plataformas(self,list_pos, plata, list_tam):
        for i in range(len(list_pos)):
            mask_plat = pygame.transform.scale(plata,list_tam[i])
            self.screen.blit(mask_plat, (list_pos[i]))
    
    # ACTIVAR LO SONIDOS
    def play_sonidos(self,sound):
        if sett.ajustes.efectos_sonidos:
            try:
                if sound == 'coins':
                    coin_sound.play()
                elif sound == 'caida':
                    error_sound.play()
                elif sound == 'salto':
                    if self.jugador.time_saltando == 0 and self.jugador.saltar:
                        salto_sound.play()
                elif sound == 'btn':
                    btn_sound.play()
                elif sound == 'click':
                    click_sound.play()
                elif sound == 'golpe':
                    golpe_sound.play()
            except:
                print("No se cargo correctamente los sonidos")
        else:
            pass
    
    def play_musica(self,music, accion):
        if sett.ajustes.efectos_sonidos:
            try:
                if music == 'menu' and accion == 'play':
                    pygame.mixer.music.load(url_menu)
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)
                elif music == 'menu' and accion == 'stop':
                    pygame.mixer.music.stop()
                elif music == 'juego' and accion == 'play':
                    pygame.mixer.music.load(url_juego)
                    pygame.mixer.music.play(-1)
                    # pygame.mixer.music.set_volume(0.5)
                elif music == 'juego' and accion == 'stop':
                    pygame.mixer.music.stop()
            except:
                print("No se cargo correctamente los sonidos")
        else:
            pass
    
    # ACTUALIZACION DE PANTALLA
    def update(self):
        pygame.display.flip()
    
    # SALIDA DEL JUEGO
    def salir_juego(self):
        pygame.quit()

