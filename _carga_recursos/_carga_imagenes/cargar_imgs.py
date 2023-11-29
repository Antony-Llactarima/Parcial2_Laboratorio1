import os
import pygame as pg

dir_actual = os.getcwd()
try:
    # PANTALLA DE INICIO (MENU) -----------------------------------
    screen_menu = pg.image.load(os.path.join(dir_actual, "recursos\imgs\_inicio\_fondo_menu.png"))
    titulo = pg.image.load(os.path.join(dir_actual,"recursos\imgs\_inicio\_titulo.png"))
    # BOTONES ----------------------------------------------------
    buttons_WaB = pg.image.load(os.path.join(dir_actual, "recursos\Sprites\_buttons\Menu Buttons sprite (BnW).png"))
    buttons_RaB = pg.image.load(os.path.join(dir_actual, "recursos\Sprites\_buttons\Menu Buttons sprite (Colored).png"))
    
    # PANTALLA DE GAME OVER --------------------------------
    screen_game_over = pg.image.load(os.path.join(dir_actual, "recursos\imgs\_game_over\_game_over_fondo.png"))
    letras_go = pg.image.load(os.path.join(dir_actual,"recursos\imgs\_game_over\_g_o_letras.png"))
    
    # PANTALLA DE VICTORIA --------------------------------
    screen_victoria = pg.image.load(os.path.join(dir_actual,"recursos\imgs\_victoria\_fondo_wins.png"))
    
    # PANTALLA DE OPCIONES ----------------------------------
    screen_options = pg.image.load(os.path.join(dir_actual, "recursos\imgs\_optiones\Sprite-0001.png"))
    
    # PANTALLA DE LOS NIVELSE --------------------------------
    fondo_nivel1 = pg.image.load(os.path.join(dir_actual, "recursos\imgs\_niveles\_forest (bosque)\_1280x720\_1.jpg"))
    fondo_nivel2 = pg.image.load(os.path.join(dir_actual, "recursos\imgs\_niveles\_forest (bosque)\_1280x720\_2.jpg"))
    fondo_nivel3 = pg.image.load(os.path.join(dir_actual,"recursos\imgs\_niveles\_forest (bosque)\_1280x720\_3.jpg"))
    
except:
    print("Error... Imagenes no cargadas.")


