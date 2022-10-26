#---Bibliotecas esenciales
import pygame as pg, sys
from pygame import *
#---Bibliotecas auxiliares
from os import path
#---Bibliotecas creadas
from button import Button
from settings import *
import settings
from level import Level

dirname = path.dirname(__file__)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pg.display.set_caption("EARTHCORE")
        self.clock = pg.time.Clock()

        #Musica del juego
        pg.mixer.music.load(dirname + "/sound/musica.mp3")
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.3)

        #Estado actual del juego
        self.game_state = "start"

        #Fondos del juego
        self.background_img = pg.image.load(dirname + "/images/backgrounds/BosqueHD.jpeg").convert_alpha()
        self.background_img = pg.transform.scale(self.background_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_config_img = pg.image.load(dirname + "/images/backgrounds/fondo_config.png").convert_alpha()
        self.background_config_img = pg.transform.scale(self.background_config_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        #Crear botones
        start_img = pg.image.load(dirname + "/images/buttons/boton_play-41X18.png").convert_alpha()#Boton de inicio
        self.start_btn = Button(0, 325, start_img, 3.4)
        self.start_btn.rect.centerx = WIDTH_SCREEN//2

        config_img = pg.image.load(dirname + "/images/buttons/config_button.png").convert_alpha()#Boton de configuración
        self.config_btn = Button(5, 5, config_img, 0.15)

        set_language_img = pg.image.load(dirname + "/images/buttons/boton_ajustes.png").convert_alpha()#Boton de ajustes de lenguajes dentro de la configuracion
        self.set_language_btn = Button(0, 100, set_language_img, 3.4)
        self.set_language_btn.rect.centerx = WIDTH_SCREEN//2

        level_1_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 1
        self.level_1_btn = Button(100, 299, level_1_img, 3.4)

        level_2_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 2
        self.level_2_btn = Button(300, 299, level_2_img, 3.4)
        self.level_2_btn.rect.centerx = WIDTH_SCREEN//2

        level_3_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 3
        self.level_3_btn = Button(0, 299, level_3_img, 3.4)
        self.level_3_btn.rect.right = WIDTH_SCREEN - 100

        back_img = pg.image.load(dirname + "/images/buttons/return_button.png").convert_alpha()#Boton de regresar
        self.back_btn = Button(0, 0, back_img, 0.13)

    def game_run(self):
        #Estado del juego
        start = "start"
        config = "config"
        level_selector = "level_selector"
        level_1 = "level_1"
        level_2 = "level_2"
        level_3 = "level_3"
        while True:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.background_img, (0, 0))

            ###  ESTADO DE INICIO  ###
            if self.game_state == start:
                if self.start_btn.draw(self.screen, play_btn_text[settings.language]):
                    self.change_state(level_selector)

                if self.config_btn.draw(self.screen):
                    self.change_state(config)
            
            ### ESTADO DE CONFIGURACIÓN ###
            if self.game_state == config:
                self.screen.blit(self.background_config_img, (0, 0))
                if self.back_btn.draw(self.screen):
                    self.change_state(start)

                if self.set_language_btn.draw(self.screen, set_language_text[settings.language]):
                    if settings.language == "english":
                        settings.language = "spanish"
                    else:
                        settings.language = "english"

            ###  ESTADO DE SELECTOR DE NIVELES  ###
            if self.game_state == level_selector:
                if self.back_btn.draw(self.screen):
                    self.change_state(start)

                if self.level_1_btn.draw(self.screen, level_1_btn_text[settings.language]):
                    self.change_state(level_1)

                if self.level_2_btn.draw(self.screen, level_2_btn_text[settings.language], False):
                    self.change_state(level_2)

                if self.level_3_btn.draw(self.screen, level_3_btn_text[settings.language], False):
                    self.change_state(level_3)

            ###  ESTADO DE INICIO DE JUEGO  ###
            if self.game_state == level_1:
                earthcore_level_1 = Level(self.screen, tile_level_1, background_level_1, frames_hongy)
                earthcore_level_1.level_run()
                self.change_state(level_selector)

            if self.game_state == level_2:
                
                self.change_state(level_selector)

            if self.game_state == level_3:
                
                self.change_state(level_selector)

            #Ultimo paso, actualizar la pantalla
            pg.display.update()

    def change_state(self, state):
        self.game_state = state

    def draw_text(self, text, color, size, pos):
        type = pg.font.SysFont("comicsanssms", size)
        textobj = type.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = pos
        self.screen.blit(textobj, textrect)

if __name__ == "__main__":
    game = Game()
    game.game_run()