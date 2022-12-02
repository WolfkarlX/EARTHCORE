#Bibliotecas necesarias
import pygame, sys
from os import path
#Bibliotecas auxiliares
from settings import *
import settings
from tiles import Tile
from items import Item
from progressBar import ProgressBar
from player import Player
from enemy import Enemy
dirname = path.dirname(__file__)
from button import Button

class Level():
    def __init__(self, screen, level_mission, level_desing, tile_grass_level, tile_dirt_level, tile_invisible, background_img, character, items, enemy, item_sound, item_back=(), item_animal=()):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.level_start_time = 0 #Para el temporizador del nivel, indicara el momento en que inicio el nivel respecto al pygame.init()
        self.current_time = 0
        self.difficulty_level = settings.time_pass_level[settings.difficulty]
        self.timer = self.set_image(Timer_img, scale= 2)
        self.timer_rect = self.timer.get_rect(topleft= (5, 5))

        self.run = False
        #Objetivo del nivel
        self.mission = level_mission
        #Definiendo fondo
        self.background = self.set_image(background_img, size= (WIDTH_SCREEN, HEIGHT_SCREEN))
        #Definiendo mapa
        self.map = self.create_map(dirname+"/"+tile_grass_level, level_desing, "X", tile_size)#Plataformas
        self.map += self.create_map(dirname+"/"+tile_dirt_level, level_desing, "U", tile_size)
        self.map += self.create_map(dirname+"/"+tile_invisible, level_desing, "I", tile_size)

        self.items = [] #Items
        for id, item in enumerate(items):
            if len(item) == 3:
                self.items.append(self.create_item(dirname+"/"+item[0], level_desing, str(id+1), item[1]))
            if len(item) == 4:
                self.items.append(self.create_item(dirname+"/"+item[0], level_desing, str(id+1), item[1], (item[2], item[3])))
        self.progressBars = [] #Barras de progreso
        for id, item in enumerate(items):
            self.progressBars.append(ProgressBar(self.set_image(item[2], size= (self.timer_rect.size)), 200, len(self.items[id]), self.screen))
        self.item_sound = pygame.mixer.Sound(item_sound)

        self.items_back = []
        if item_back:
            self.items_back = self.create_item(dirname+"/"+item_back[0], level_desing, "T", item_back[1]) #Items de fondo, el jugador no interactua
        
        self.enemies = self.create_enemies(enemy[0], level_desing, "Y", enemy[1], enemy[2])#Enemigos

        self.scroll_map = 0
        #Definiendo personaje
        self.player = Player(character[0], character[1], character[2], character[3], character[4], character[5])
        self.dead_sound = pygame.mixer.Sound(dead_sound_effect)
        
        #Fondos      
        self.backround_controls =  pygame.image.load(dirname + background_controls_img)
        self.backround_controls = pygame.transform.scale(self.backround_controls,(WIDTH_SCREEN, HEIGHT_SCREEN))

        #Creacion de Botones
        self.control_button_control_img = pygame.image.load(dirname + control_button_btn).convert_alpha()
        self.control_btn = Button(0, 0, self.control_button_control_img, 0.4)
        self.control_btn.rect.bottomright = (WIDTH_SCREEN, HEIGHT_SCREEN)

        back_img = pygame.image.load(dirname + "/images/buttons/return_button.png").convert_alpha()
        self.back_btn = Button(0, 0, back_img, 0.13)

        out_img = pygame.image.load(dirname + "/images/buttons/Boton Salir.png")
        self.out_btn = Button(0, 5, out_img, 2.8)
        self.out_btn.rect.right = WIDTH_SCREEN - 5

        return_img = pygame.image.load(dirname + "/images/buttons/Boton Play.png")
        self.return_btn = Button(0, 5, return_img, 2.8)
        self.return_btn.rect.right = self.out_btn.rect.left - 5

        pause_img = pygame.image.load(dirname + "/images/buttons/boton pause.png")
        self.pause_btn = Button(0, 5, pause_img, 2.8)
        self.pause_btn.rect.right = self.out_btn.rect.left - 5

        set_volume_on_image = pygame.image.load(dirname + "/images/buttons/Icono_con_volumen.png").convert_alpha()
        self.set_volume_on_btn = Button(0, 0, set_volume_on_image, 0.8)
        self.set_volume_on_btn.rect.midright = (WIDTH_SCREEN - 5, HEIGHT_SCREEN//2)

        set_volume_off_image = pygame.image.load(dirname + "/images/buttons/Icono_sin_volumen.png").convert_alpha()
        self.set_volume_off_btn = Button(0, 0, set_volume_off_image, 0.8)
        self.set_volume_off_btn.rect.midright = (WIDTH_SCREEN - 5, HEIGHT_SCREEN//2)

    def level_run(self):
        self.run = True
        self.level_start_time = pygame.time.get_ticks() #Obteniendo el tiempo justo antes de iniciar el nivel
        while self.run:
            #Control del tiempo en el nivel
            self.clock.tick(60)
            self.current_time = pygame.time.get_ticks()#Obtiene el momento actual
            #Eventos
            self.level_events()
            self.player.eventos_teclado()
            #Dibujar Fondo del nivel
            self.screen.blit(self.background, (0, 0))
            #Dibujar Escenario del nivel
            for tile in self.map:
                tile.rect.x -= self.scroll_map
                self.screen.blit(tile.image, tile.rect.topleft)
            
            for group_item in self.items:
                for item in group_item:
                    item.rect.x -= self.scroll_map
                    self.screen.blit(item.image, item.rect.topleft)
            
            for back in self.items_back:
                back.rect.x -= self.scroll_map
                self.screen.blit(back.image, back.rect.topleft)
            
            for enemy in self.enemies:
                enemy.rect.x -= self.scroll_map
                enemy.pos_ini[0] -= self.scroll_map
                enemy.dibujar(self.screen)
                
            self.scroll_map = 0
            
            ###Logica Jugador
            self.player.actualizar()
            #Colision con un bloque
            for tile in self.map:
                if self.player.rect.colliderect(tile):
                    if self.player.rect.bottom < tile.rect.centery and self.player.rect.bottom-self.player.vel_y <= tile.rect.top+5 and self.player.vel_y >= 0:
                        self.player.rect.bottom = tile.rect.top+5
                        self.player.en_tierra = True
                    elif self.player.rect.top > tile.rect.centery and self.player.vel_y < 0 and self.player.rect.right > tile.rect.left+self.player.vel_x and self.player.rect.left < tile.rect.right+self.player.vel_x:
                        self.player.rect.top = tile.rect.bottom
                        self.player.vel_y = 0
                    elif self.player.rect.right > tile.rect.left and self.player.rect.left < tile.rect.right:
                        if self.player.rect.right < tile.rect.centerx:
                            self.player.rect.right = tile.rect.left
                        if self.player.rect.left > tile.rect.centerx:
                            self.player.rect.left = tile.rect.right
            #Recoger items
            for id, group_item in enumerate(list(self.items)):
                for item in group_item:
                    if self.player.rect.collidepoint(item.rect.center):
                        if item.replacement:
                            self.items_back.append(Item((item.rect.x - (item.replacement[1][0]-item.rect.width)//2, item.rect.y - (item.replacement[1][1]-item.rect.height)), item.replacement[1], item.replacement[0], "T"))
                        self.items[id].remove(item)
                        self.progressBars[id].add_part()
                        self.item_sound.play()

            #Colision con enemigo
            for enemy in self.enemies:
                if self.player.rect.colliderect(enemy):
                    self.dead()
                   

            #Logica Jugador-Mapa
            if self.player.rect.centerx > 600:
                self.player.rect.centerx = 600
                self.scroll_map += self.player.vel

            if self.player.rect.centerx < 300:
                self.player.rect.centerx = 300
                self.scroll_map -= self.player.vel
            
            #Dibujar Jugador   
            self.player.dibujar(self.screen)

            #### Interfaz, la interfaz ira por encima de todo
            #Mostrar el temporizador
            time_left = self.difficulty_level - (self.current_time - self.level_start_time)//1000
            nextInterface = self.show_timer(time_left)
            if time_left == 0: #Si el tiempo restante es 0 se acaba el nivel
               self.dead()

            for bar in self.progressBars:
                nextInterface = bar.draw_progress_bar(nextInterface)
            
            self.draw_label(self.mission, (255,255,255),(0,0,0),16,topleft=(10,50))
            self.draw_label(Pause_txt[settings.language],(255,255,255), (0,0,0,), 16, topright=(WIDTH_SCREEN - 170,5))
            if self.pause_btn.draw(self.screen):
                self.stop()
            #Actualizar pantalla
            pygame.display.flip()

            #Caer del mapa
            if self.player.rect.top > HEIGHT_SCREEN:
                self.dead()

            #Parametros para ganar
            no_items = True
            for group_item in self.items:
                if group_item:
                    no_items = False
            if no_items:
                return True
        
        return False

    def level_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                if event.key == pygame.K_p:
                    self.stop()
    
    def set_image(self, dir, scale = 0, size = 0):
        back = pygame.image.load(dirname + "/" + dir).convert_alpha()
        if scale:
            back = pygame.transform.scale(back, (back.get_size()[0] * scale, back.get_size()[1] * scale))
        if size:
            back = pygame.transform.scale(back, size)
        return back

    def stop(self): #Funcion para hacer la pausa
        pause_surface = self.screen.copy() #Copia la pantalla para mostrarla como fondo
        self.return_btn.clicked = True #El atributo clicked se hace True porque este boton esta encima de otro, el de pausa
        init_pause = pygame.time.get_ticks()#Se obtiene el momento en el que se hizo la pausa
        paus = True
        self.game_state = pause
        while paus:
            self.screen.blit(pause_surface, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if self.game_state == pause:
                        if event.key == pygame.K_r:
                            paus = False
                            self.level_start_time += pygame.time.get_ticks() - init_pause #El momento en el que inicio el nivel se le suma el tiempo que duro el juego en pausa
                            self.pause_btn.clicked = True
                    if self.game_state == pause or self.game_state == start and not controls:
                        if event.key == pygame.K_q:
                            paus = False
                            self.run = False

            if self.game_state == pause:
                rect_pause = self.txt(settings.level_pause_text[settings.language], 120, center=(WIDTH_SCREEN//2, HEIGHT_SCREEN//2-50))
                self.txt(settings.press_Q_text[settings.language], 30, topleft=(20, HEIGHT_SCREEN-50))
                self.txt(settings.press_R_text[settings.language], 30, center=(rect_pause.centerx, rect_pause.centery+100))
                if self.return_btn.draw(self.screen):
                    paus = False
                    self.level_start_time += pygame.time.get_ticks() - init_pause
                    self.pause_btn.clicked = True #Boton de pausa encima de regresar, se considera clicked True
                    
                if self.out_btn.draw(self.screen):
                    self.run = False
                    paus = False
                if pygame.mixer.music.get_busy():
                    if self.set_volume_on_btn.draw(self.screen):
                        pygame.mixer.music.stop()
                else:
                    if self.set_volume_off_btn.draw(self.screen):
                        pygame.mixer.music.play(-1)
                if self.control_btn.draw(self.screen):
                    self.change_state(controls)

            if self.game_state == controls:
                self.screen.blit(self.backround_controls, (0, 0))
                if self.back_btn.draw(self.screen):
                    self.change_state(pause)
            pygame.display.flip()

    def txt(self, texto, tam, topleft=(), topright=(), center=(), midleft=()): #Crear texto con fuente comic sans mc
        tex = pygame.font.SysFont("comic sans ms", tam)
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
       

    def create_but(self,dire): #crear botones
        button = pygame.image.load(dire).convert_alpha()
        self.button_btn = Button(0, 10, button, 0.30)
        self.button_btn.rect.x = self.screen.get_width() - 200
        
        self.game_state = pause
        if self.button_btn.draw(self.screen):
            self.change_state(pause)
            if self.game_state == pause:
                img = pygame.image.load(dirname + dire)
                img = pygame.transform.scale(img,(WIDTH_SCREEN, HEIGHT_SCREEN).convert_alpha())
                self.screen.blit(img,(0,0))
      

    def change_state(self, state): #Cambiar de estados 
        self.game_state = state

    def create_map(self, img_dir, desing_map, letter, size):
        map = []
        for row_index, row in enumerate(desing_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == letter:
                    map.append(Tile((x, y), size, img_dir))
        return map
    
    def create_item(self, img_dir, desing_map, letter, size, replacement=()):
        items = []
        for row_index, row in enumerate(desing_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == letter:
                    items.append(Item((x+(tile_size-size[0])/2, y+(tile_size-size[1])), size, img_dir, letter, replacement))
        return items

    def create_enemies(self, image_dir, desing_map, letter, dim, route):
        enemies = []
        for row_index, row in enumerate(desing_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == letter:
                    enemies.append(Enemy(image_dir, dim, (x, y+(tile_size-dim[1])), route))
        return enemies

    def show_timer(self, time):
        type = pygame.font.SysFont("consolas", self.timer_rect.height-2)
        textobj_out = type.render("{:02d}:{:02d}".format(time//60, time%60), True, BLACK)
        textrect_out = textobj_out.get_rect(midleft= self.timer_rect.midright)
        textrect_out.x += 5

        textobj_in = type.render("{:02d}:{:02d}".format(time//60, time%60), True, WHITE)
        textrect_in = textobj_in.get_rect(midleft= self.timer_rect.midright)
        textrect_in.x += 5

        self.screen.blit(self.timer, self.timer_rect)
        self.screen.blit(textobj_out, (textrect_out.x+1, textrect_out.y-1))
        self.screen.blit(textobj_out, (textrect_out.x+1, textrect_out.y+1))
        self.screen.blit(textobj_out, (textrect_out.x-1, textrect_out.y-1))
        self.screen.blit(textobj_out, (textrect_out.x-1, textrect_out.y+1))
        self.screen.blit(textobj_in, textrect_in)

        textrect_in.x += 15
        return textrect_in.midright
    
    def dead(self): #pantalla muerte de personaje
        music = pygame.mixer.music.get_busy()
        if music:
            pygame.mixer.music.pause()
        self.dead_sound.play()
        pausex = True
        while pausex:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pausex = False
                        self.run = False
                        self.dead_sound.stop()
                        if music:
                            pygame.mixer.music.unpause()
            
            self.screen.fill(0)
            self.print_hongy()
            self.txt(settings.level_GAME_OVER_text[settings.language], 60, center=(WIDTH_SCREEN//2, HEIGHT_SCREEN//2+100))
            self.txt(settings.press_ESC_text[settings.language], 30, topleft=(20, HEIGHT_SCREEN-50))
            if self.out_btn.draw(self.screen):
                pausex = False
                self.run = False
                self.dead_sound.stop()
                if music:
                    pygame.mixer.music.unpause()
            pygame.display.flip()
           
    #def print_hongy(self):
        #timer, pa = 0, 100
        #timer += 1
        #sprites = []
        
        #for n in range(1,7):
            #hongy_llorando = pygame.image.load(f"images/hongy/HongyLlorando{n}.png")
            #hongy_llorando = pygame.transform.scale(hongy_llorando,(WIDTH_SCREEN,HEIGHT_SCREEN))
            
            #sprites.append(hongy_llorando)
        
        #if timer >= pa:
            #self.screen.blit(sprites[indice],(0,0))
            #indice += 1
            #timer = 0
            #if indice >= len(sprites):
                #indice = 0
        #pygame.display.update()

    def draw_label(self, text, color, backcolor=BLACK, size=False, topleft=(), topright=(), center=(), midleft=()):
        if not size:
            font = pygame.font.SysFont("consolas", 0)
        else:
            font = pygame.font.SysFont("consolas", size)
        textobj = font.render(text, True, color)
        texrect = textobj.get_rect()
        if topleft:
            texrect.topleft = topleft
        elif topright:
            texrect.topright = topright
        elif center:
            texrect.center = center
        elif midleft:
            texrect.midleft = midleft

        pygame.draw.rect(self.screen, backcolor, ((texrect.x-15, texrect.y), (texrect.width+24, texrect.height)), border_radius=10)   
        self.screen.blit(textobj,texrect)
        return texrect
    
    def print_hongy(self):
        hongy_llorando = pygame.image.load( dirname +"/images/hongy/HongyLlorando5.png")
        hongy_llorando = pygame.transform.scale(hongy_llorando,(300,300))
        self.screen.blit(hongy_llorando, (WIDTH_SCREEN /2 -150, HEIGHT_SCREEN //2 - 270))
        
