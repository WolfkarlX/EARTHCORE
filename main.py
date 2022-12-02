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

        # Musica del juego
        pg.mixer.music.load(dirname + "/sound/music/prueba_music.wav")
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.04)

        #Estado actual del juego
        self.game_state = "start"

        #Fondos del juego
        self.background_img = pg.image.load(dirname + "/images/backgrounds/BosqueHD.jpeg").convert_alpha()
        self.background_img = pg.transform.scale(self.background_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_config_img = pg.image.load(dirname + "/images/backgrounds/fondo_config.png").convert_alpha()
        self.background_config_img = pg.transform.scale(self.background_config_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_controls_img = pg.image.load(dirname + "/images/backgrounds/Fondo Controles.png").convert_alpha()
        self.background_controls_img = pg.transform.scale(self.background_controls_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_lore_img = pg.image.load(dirname + "/images/backgrounds/lore.png").convert_alpha()
        self.background_lore_img = pg.transform.scale(self.background_lore_img, (WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_level_1_finished = pg.image.load(dirname + background_level_1_finished)
        self.background_level_1_finished = pg.transform.scale(self.background_level_1_finished,(WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_level_3_finished = pg.image.load(dirname + background_level_3_finished)
        self.background_level_3_finished = pg.transform.scale(self.background_level_3_finished,(WIDTH_SCREEN, HEIGHT_SCREEN))

        self.background_lore1_img = pg.image.load(dirname + "/images/backgrounds/lore.png")   
        self.background_lore1_img = pg.transform.scale(self.background_lore1_img,(WIDTH_SCREEN, HEIGHT_SCREEN))     

        #Crear botones
        start_img = pg.image.load(dirname + "/images/buttons/boton_play-41X18.png").convert_alpha()#Boton de inicio
        self.start_btn = Button(0, 450, start_img, 3.4)
        self.start_btn.rect.centerx = WIDTH_SCREEN//2

        config_img = pg.image.load(dirname + "/images/buttons/config_button.png").convert_alpha()#Boton de configuración
        self.config_btn = Button(5, 5, config_img, 0.15)

        set_language_img = pg.image.load(dirname + "/images/buttons/boton_ajustes.png").convert_alpha()#Boton de ajustes de lenguajes dentro de la configuracion
        self.set_language_btn = Button(0, 100, set_language_img, 3.4)
        self.set_language_btn.rect.centerx = WIDTH_SCREEN//2 - 120

        set_mode_img = pg.image.load(dirname + "/images/buttons/boton_ajustes.png").convert_alpha()#Boton de ajustes de dificultad dentro de la configuracion
        self.set_mode_btn = Button(0, 0, set_mode_img, 3.4)
        self.set_mode_btn.rect.center = (self.set_language_btn.rect.centerx, self.set_language_btn.rect.centery + 100)

        set_volume_on_image = pg.image.load(dirname + "/images/buttons/Icono_con_volumen.png").convert_alpha()#Boton de musica activa
        self.set_volume_on_btn = Button(0, 0, set_volume_on_image, 0.8)
        self.set_volume_on_btn.rect.center = (self.set_mode_btn.rect.centerx, self.set_mode_btn.rect.centery + 120)

        set_volume_off_image = pg.image.load(dirname + "/images/buttons/Icono_sin_volumen.png").convert_alpha()#Boton de musica inactiva
        self.set_volume_off_btn = Button(0, 0, set_volume_off_image, 0.8)
        self.set_volume_off_btn.rect.center = (self.set_mode_btn.rect.centerx, self.set_mode_btn.rect.centery + 120)

        level_1_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 1
        self.level_1_btn = Button(100, 450, level_1_img, 3.4)

        level_2_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 2
        self.level_2_btn = Button(300, 450, level_2_img, 3.4)
        self.level_2_btn.rect.centerx = WIDTH_SCREEN//2

        level_3_img = pg.image.load(dirname + "/images/buttons/boton_niveles.png").convert_alpha()#Boton de nivel 3
        self.level_3_btn = Button(0, 450, level_3_img, 3.4)
        self.level_3_btn.rect.right = WIDTH_SCREEN - 100

        control_button_img = pg.image.load(dirname + "/images/buttons/controles_boton.png").convert_alpha()#Boton de controles
        self.control_button_btn = Button(self.screen.get_width(), 7, control_button_img, 0.34)
        self.control_button_btn.rect.x -= self.control_button_btn.rect.width +15

        book_button_img = pg.image.load(dirname + "/images/buttons/lore_boton.png").convert_alpha()#Boton de lore
        self.book_button_btn = Button(0, 0, book_button_img, 0.18)
        self.book_button_btn.rect.right = self.control_button_btn.rect.left - 15

        back_img = pg.image.load(dirname + "/images/buttons/return_button.png").convert_alpha()#Boton de regresar
        self.back_btn = Button(0, 0, back_img, 0.13)

        out_img = pg.image.load(dirname + "/images/buttons/Boton Salir.png")
        self.out_btn = Button(0, 5, out_img, 2.8)
        self.out_btn.rect.right = WIDTH_SCREEN - 30

        next_img = pg.image.load(dirname + "/images/buttons/flecha_next.png")
        self.next_btn = Button(0, 0, next_img, 1)
        self.next_btn.rect.right = WIDTH_SCREEN - 20
        self.next_btn.rect.bottom = HEIGHT_SCREEN - 10 

        before_img = pg.image.load(dirname + "/images/buttons/flecha_next.png")
        before_img = pg.transform.flip(before_img, True, False)
        self.before_btn = Button(0, 0, before_img, 1)
        self.before_btn.rect.left = 10
        self.before_btn.rect.bottom = HEIGHT_SCREEN - 10 

    def game_run(self):
      
        #Bucle Pirncipal
        while True:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                        
            self.screen.blit(self.background_img,(0,0))

            ###  ESTADO DE INICIO  ###
            if self.game_state == start:
                if self.start_btn.draw(self.screen, play_btn_text[settings.language]):
                    self.change_state(level_selector)

                if self.config_btn.draw(self.screen):
                    self.change_state(config)
            
            ### ESTADO DE CONFIGURACIÓN ###
            elif self.game_state == config:
                self.screen.blit(self.background_config_img,(0,0))
                if self.back_btn.draw(self.screen):
                    self.change_state(start)

                if self.set_language_btn.draw(self.screen, set_language_text[settings.language]):
                    if settings.language == "english":
                        settings.language = "spanish"
                    else:
                        settings.language = "english"
                self.draw_label(label_language_text[settings.language], WHITE, self.set_language_btn.rect)

                if self.set_mode_btn.draw(self.screen, set_mode_text[settings.language][settings.difficulty]):
                    if settings.difficulty == "easy":
                        settings.difficulty = "hard"
                    elif settings.difficulty == "hard":
                        settings.difficulty = "easy"
                self.draw_label(label_mode_text[settings.language], WHITE, self.set_mode_btn.rect)

                if pg.mixer.music.get_busy():
                    if self.set_volume_on_btn.draw(self.screen):
                        pg.mixer.music.stop()
                else:
                    if self.set_volume_off_btn.draw(self.screen):
                        pg.mixer.music.play(-1)
                self.draw_label(label_music_text[settings.language], WHITE, self.set_volume_on_btn.rect, size=self.set_mode_btn.rect.height//10*7)

            ###  ESTADO DE SELECTOR DE NIVELES  ###
            elif self.game_state == level_selector:
                if self.back_btn.draw(self.screen):
                    self.change_state(start)

                if self.level_1_btn.draw(self.screen, level_1_btn_text[settings.language]):
                    self.change_state(level_1)

                if self.level_2_btn.draw(self.screen, level_2_btn_text[settings.language], settings.open_level_2):
                    self.change_state(level_2)

                if self.level_3_btn.draw(self.screen, level_3_btn_text[settings.language], settings.open_level_3):
                    self.change_state(level_3)

                if self.control_button_btn.draw(self.screen):
                    self.change_state(controls)

                if self.book_button_btn.draw(self.screen):
                    self.change_state(lore)
            
            ###  ESTADO DE CONTROLES DEL JUEGO  ###
            elif self.game_state == controls:
                self.screen.blit(self.background_controls_img, (0, 0))

                if self.back_btn.draw(self.screen):
                    self.change_state(level_selector)
            
            ## ESTADO DE LORE DEL JUEGO ##
            elif self.game_state == lore:
                self.screen.blit(self.background_lore_img, (0, 0))
                if self.next_btn.draw(self.screen):
                    self.change_state(lore1)

                if self.back_btn.draw(self.screen):
                    self.change_state(level_selector)
            elif self.game_state == lore1:
                self.screen.blit(self.background_lore_img, (0, 0))
                if self.before_btn.draw(self.screen):
                    self.change_state(lore)
            ###  ESTADO DE INICIO DE NIVEL  ###
            elif self.game_state == level_1:
                earthcore_level_1 = Level(self.screen, objetive_level_1_text[settings.language], level_map_1, tile_grass_level_1, tile_dirt_level_1, tile_invisible, background_level_1, character_level_1, items_level_1, enemy_level_1, item_sound_effect_level_1, item_back= item_back_level_1)
                if earthcore_level_1.level_run():
                    self.ganar(self.background_level_1_finished,WIDTH_SCREEN//2, HEIGHT_SCREEN//2 -200, WIDTH_SCREEN//2, HEIGHT_SCREEN//2 -150, settings.level_completed_text, 60, settings.level_completed_text1, 30)
                    settings.open_level_2 = True
                self.change_state(level_selector)

            elif self.game_state == level_2:
                earthcore_level_2 = Level(self.screen, objetive_level_2_text[settings.language], level_map_2, tile_grass_level_2, tile_dirt_level_2, tile_invisible, background_level_2, character_level_2, items_level_2, enemy_level_2, item_sound_effect_level_2)
                if earthcore_level_2.level_run():
                    settings.open_level_3 = True
                self.change_state(level_selector)

            elif self.game_state == level_3: 
                earthcore_level_3 = Level(self.screen, objetive_level_3_text[settings.language], level_map_3, tile_grass_level_3, tile_dirt_level_3, tile_invisible, background_level_3, character_level_3, items_level_3, enemy_level_3, item_sound_effect_level_3, item_back=  item_back_level_3)
                if True: #earthcore_level_3.level_run():
                    self.ganar(self.background_level_3_finished, WIDTH_SCREEN//2, HEIGHT_SCREEN//2, WIDTH_SCREEN//2, HEIGHT_SCREEN//2 -100, settings.level_completed_text3, 60, settings.level_completed_text4, 60)
                self.change_state(level_selector)

            #Ultimo paso, actualizar la pantalla
            pg.display.update()

    def change_state(self, state):
        self.game_state = state
    

    def draw_label(self, text, color, rect, backcolor=BLACK, size=False):
        if not size:
            font = pg.font.SysFont("consolas", rect.height//10*7)
        else:
            font = pg.font.SysFont("consolas", size)
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.midright = (rect.left-15, rect.centery)

        pg.draw.rect(self.screen, backcolor, ((textrect.x-12, textrect.y), (textrect.width+24, textrect.height)), border_radius=10)
        self.screen.blit(textobj, textrect)

    def ganar(self, image, x, y, x1, y1, txt, tam, txt1, tam1):# Bucle que muestra pantalla despues de ganar 
        pausex = True
        while pausex:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pausex = False
            self.screen.blit(image,(0,0))
            self.txt(txt[settings.language], tam, center=(x, y))
            self.txt(txt1[settings.language], tam1, center=(x1, y1))
            self.txt(level_completed_text2[settings.language], 30, topleft=(20, HEIGHT_SCREEN-50))
            if self.out_btn.draw(self.screen):
                pausex = False
            pg.display.flip()
    
    def txt(self, texto, tam, topleft=(), topright=(), center=(), midleft=()): #Crear texto con fuente comic sans mc
        tex = pg.font.SysFont("comic sans ms", tam)
        tex = tex.render(texto, 1,(255,255,255))
        texrect = tex.get_rect()
        if topleft:
            texrect.topleft = topleft
        elif topright:
            texrect.topright = topright
        elif center:
            texrect.center = center
        elif midleft:
            texrect.midleft = midleft
        self.screen.blit(tex, texrect)
        
        return texrect

if __name__ == "__main__":
    game = Game()
    game.game_run()