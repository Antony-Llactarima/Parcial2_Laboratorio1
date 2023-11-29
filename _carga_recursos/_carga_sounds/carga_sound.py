import pygame
import os

dir_actual = os.getcwd()

pygame.mixer.init()
try:
    coin_sound = pygame.mixer.Sound(os.path.join(dir_actual,"recursos\_sounds\coin_c_02-102844.mp3"))
    coin_sound.set_volume(0.5)

    error_sound = pygame.mixer.Sound(os.path.join(dir_actual,"recursos\_sounds\error-126627.mp3"))
    error_sound.set_volume(0.5)

    salto_sound = pygame.mixer.Sound(os.path.join(dir_actual,"recursos\_sounds\sfx_jump_07-80241.mp3"))
    salto_sound.set_volume(0.5)

    btn_sound = pygame.mixer.Sound(os.path.join(dir_actual,"recursos\_sounds\digital-beeping-151921.mp3"))
    btn_sound.set_volume(0.5)

    click_sound = pygame.mixer.Sound(os.path.join(dir_actual,"recursos\_sounds\click-menu-app-147357 (1).mp3"))
    click_sound.set_volume(0.5)
except:
    print("No se cargo los sonidos correctamente.")