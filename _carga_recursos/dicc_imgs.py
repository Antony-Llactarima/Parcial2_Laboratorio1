from _carga_recursos._carga_imagenes.cargar_imgs import *
import pygame as pg

# TAMANIO DE LA VENTANA DEL JUEGO
t_screen = (1080,720)

# FONDOS PARA LAS DISTINTAS PANTALLAS:
fondos = {
    'menu': screen_menu,
    'game_over': screen_game_over,
    'options': screen_options,
    'victoria': screen_victoria,
    'selecc_nivel': screen_menu
}

# FONDOS DE LOS NIVELES
fondos_niveles = {}
for i in range(3):
    if i == 0:
        fondo_nivel = pg.transform.scale(fondo_nivel1,(t_screen[0],t_screen[1]))
        fondos_niveles['nivel_1'] = fondo_nivel
    elif i == 1:
        fondo_nivel = pg.transform.scale(fondo_nivel2,(t_screen[0],t_screen[1]))
        fondos_niveles['nivel_2'] = fondo_nivel
    else:
        fondo_nivel = pg.transform.scale(fondo_nivel3,(t_screen[0],t_screen[1]))
        fondos_niveles['nivel_3'] = fondo_nivel

# TITULO E IMAGEN DE GAME OVER Y EXTRAS
img_extras = {}

img_extras['titulo'] = pg.transform.scale(titulo,(700,400))
img_extras['game_over'] = pg.transform.scale(letras_go, (600,300))

# FUNCION PARA OBTENER LOS BOTONES
def obtener_btns_largos(pos_x, pos_y, png_btns):
    tam_btn_large = [250,100]
    png_btns.set_clip((pos_x,pos_y,610,210))
    btn = png_btns.subsurface(png_btns.get_clip())
    btn = pg.transform.scale(btn,(tam_btn_large[0],tam_btn_large[1]))
    return btn

# IMAGENES DE LOS BOTONES LARGOS EN BLANCO Y NEGRO
b_WaB_large = {}
b_WaB_large['play'] = obtener_btns_largos(0,0,buttons_WaB)
b_WaB_large['resume'] = obtener_btns_largos(0,210,buttons_WaB)
b_WaB_large['ajuste'] = obtener_btns_largos(1210,410,buttons_WaB)
b_WaB_large['exit'] = obtener_btns_largos(1210,620,buttons_WaB)
b_WaB_large['newGame'] = obtener_btns_largos(0,610,buttons_WaB)
b_WaB_large['menu'] = obtener_btns_largos(1210,210,buttons_WaB)
b_WaB_large['back'] = obtener_btns_largos(0,840,buttons_WaB)
b_WaB_large['continue'] = obtener_btns_largos(610,210,buttons_WaB)

# IMAGENES DE LOS BOTONES LARGOS EN ROJO Y NEGRO
b_RaB_large = {}
b_RaB_large['play'] = obtener_btns_largos(0,0,buttons_RaB)
b_RaB_large['resume'] = obtener_btns_largos(0,210,buttons_RaB)
b_RaB_large['ajuste'] = obtener_btns_largos(1210,410,buttons_RaB)
b_RaB_large['exit'] = obtener_btns_largos(1210,620,buttons_RaB)
b_RaB_large['newGame'] = obtener_btns_largos(0,610,buttons_RaB)
b_RaB_large['menu'] = obtener_btns_largos(1210,210,buttons_RaB)
b_RaB_large['back'] = obtener_btns_largos(0,840,buttons_RaB)
b_RaB_large['continue'] = obtener_btns_largos(610,210,buttons_RaB)

# ----------------------------------------------------------------
# 

# FUNCION PARA OBTENER BOTONES CORTOS EN BLANCO Y NEGRO
def obtener_btns_cortos(pos_x, pos_y, png_btns):
    tam_btn_corto = [100,100]
    png_btns.set_clip((pos_x,pos_y,200,200))
    btn = png_btns.subsurface(png_btns.get_clip())
    btn = pg.transform.scale(btn,(tam_btn_corto[0],tam_btn_corto[1]))
    return btn

# DICCIONARIOS DE LOS BOTONES CORTOS BLANCO Y NEGRO
b_WaB_cortos = {}
b_WaB_cortos['music'] = obtener_btns_cortos(2040,630,buttons_WaB)
b_WaB_cortos['sound'] = obtener_btns_cortos(1830,630,buttons_WaB)
b_WaB_cortos['cross'] = obtener_btns_cortos(820,840,buttons_WaB)
b_WaB_cortos['check'] = obtener_btns_cortos(610,840,buttons_WaB)

b_RaB_cortos = {}
b_RaB_cortos['music'] = obtener_btns_cortos(2040,630,buttons_RaB)
b_RaB_cortos['sound'] = obtener_btns_cortos(1830,630,buttons_RaB)
b_RaB_cortos['cross'] = obtener_btns_cortos(820,840,buttons_RaB)
b_RaB_cortos['check'] = obtener_btns_cortos(610,840,buttons_RaB)

# ----------------------------------------------------------------
img_selec_nivel = {}

img_selec_nivel['nivel_1'] = pg.transform.scale(fondo_nivel1,(180,200))
img_selec_nivel['nivel_2'] = pg.transform.scale(fondo_nivel2,(180,200))
img_selec_nivel['nivel_3'] = pg.transform.scale(fondo_nivel3,(180,200))
