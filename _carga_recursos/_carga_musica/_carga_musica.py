import pygame
import os

dir_actual = os.getcwd()
pygame.mixer.init()

try:
    url_menu = os.path.join(dir_actual,"recursos\_musicas\i-am-dreaming-or-final-fantasy-menu-kinda-thing-29173.mp3")
    url_juego = os.path.join(dir_actual,"recursos\_musicas\_ranas-en-la-laguna-magica-melodia-videojuego-indie-114116.mp3")
except:
    pass