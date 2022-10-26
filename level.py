#Bibliotecas necesarias
import pygame, sys
from os import path
#Bibliotecas auxiliares
from settings import *
from tiles import Tile
from player import Player

dirname = path.dirname(__file__)

class Level():
    def __init__(self, screen, tile_level, background_img, character):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.run = False
        #Definiendo fondo
        self.background = self.set_image(background_img, 0, (WIDTH_SCREEN, HEIGHT_SCREEN))
        #Definiendo mapa
        self.map = self.create_map(dirname+"/"+tile_level, level_map_1)
        self.scroll_map = 0
        #Definiendo personaje
        self.player = Player(character, 30, 30, (200, 200))

    def level_run(self):
        self.run = True
        while self.run:
            self.clock.tick(60)
            #Eventos
            self.level_events()
            #Fondo del nivel
            self.screen.blit(self.background, (0, 0))
            #Escenario del nivel
            for tile in self.map:
                tile.rect.x -= self.scroll_map
                self.screen.blit(tile.image, tile.rect.topleft)
            self.scroll_map = 0
            
            #Jugador
            self.player.actualizar()
            
            for tile in self.map:
                if self.player.rect.colliderect(tile):
                    if self.player.rect.bottom < tile.rect.centery and self.player.rect.right > tile.rect.left and self.player.rect.left < tile.rect.right:
                        self.player.rect.bottom = tile.rect.top+5
                        self.player.en_tierra = True
                    elif self.player.rect.top > tile.rect.centery and self.player.rect.right > tile.rect.left and self.player.rect.left < tile.rect.right:
                        self.player.vel_y = self.player.gravedad
                    elif self.player.rect.right > tile.rect.left and self.player.rect.left < tile.rect.right:
                        if self.player.direccion:
                            self.player.rect.right = tile.rect.left
                        else:
                            self.player.rect.left = tile.rect.right
                   
                    
            self.player.dibujar(self.screen)

            if self.player.rect.centerx > 600:
                self.player.rect.centerx = 600
                self.scroll_map += self.player.vel

            if self.player.rect.centerx < 300:
                self.player.rect.centerx = 300
                self.scroll_map -= self.player.vel
            #Actualizar pantalla
            pygame.display.flip()

    def level_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
            self.player.eventos(event)

    def set_image(self, dir, scale = 0, size = 0):
        back = pygame.image.load(dirname + "/" + dir).convert_alpha()
        if scale:
            back = pygame.transform.scale(back, (back.get_size()[0] * scale, back.get_size()[1] * scale))
        if size:
            back = pygame.transform.scale(back, size)
        return back

    def create_map(self, img_dir, desing_map):
        map = []
        for row_index, row in enumerate(desing_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == "X":
                    map.append(Tile((x, y), tile_size, img_dir))
        return map