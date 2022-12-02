import pygame 
import settings

class Player():
    def __init__(self, image_dir, width, height, pos, jump_power, width_ajust= 0):
        self.image = []
        self.frames = 0
        for id, img in enumerate(image_dir):
            self.image.append(pygame.image.load(img).convert_alpha())
            self.frames += 1
        for id, img in enumerate(self.image):
            self.image[id] = pygame.transform.scale(img, (width, height))
        self.rect = self.image[0].get_rect(topleft= pos)
        self.rect.width -= width_ajust
        self.width_ajust = width_ajust

        self.player_jump = jump_power
        self.player_jump_sound = pygame.mixer.Sound(settings.jump_sound)
        self.caminando = False
        self.en_tierra = False
        self.direccion = True
        self.gravedad = 10
        
        self.frame_actual = 0
        self.frame_count = 0

        self.vel_x = 0
        self.vel_y = 0
        self.vel = 6
    
    def eventos_teclado(self):
        keyword = pygame.key.get_pressed()
        if keyword[pygame.K_SPACE]  and self.en_tierra == True:
            self.vel_y = self.player_jump
            self.en_tierra = False
            self.player_jump_sound.play()
        if keyword[pygame.K_RIGHT] and keyword[pygame.K_LEFT] or keyword[pygame.K_d] and keyword[pygame.K_a]:
            self.vel_x = 0
            self.frame_actual = 0
            self.caminando = False
        elif keyword[pygame.K_LEFT] or keyword[pygame.K_a] :
            self.direccion = False
            self.caminando = True
            self.vel_x = -self.vel
        elif keyword[pygame.K_RIGHT] or keyword[pygame.K_d]:
            self.direccion = True
            self.caminando = True
            self.vel_x = self.vel
        else: 
            self.vel_x = 0
            self.frame_actual = 0
            self.caminando = False

    def actualizar(self):
        if self.en_tierra:
            self.vel_y = 0
        else:
            self.vel_y += 1
            if self.vel_y > self.gravedad:
                self.vel_y = self.gravedad
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.en_tierra = False

    def dibujar(self, screen):
        if self.en_tierra:
            if self.caminando:
                self.frame_count += 1
                if self.frame_count > 5:
                    self.frame_actual += 1
                    self.frame_count = 0
                    if self.frame_actual >= self.frames-1:
                        self.frame_actual = 0
                screen.blit(pygame.transform.flip(self.image[self.frame_actual], self.direccion, False), (self.rect.left-self.width_ajust//2, self.rect.top))
            else:
                screen.blit(pygame.transform.flip(self.image[0], self.direccion, False), (self.rect.left-self.width_ajust//2, self.rect.top))
        else:
            screen.blit(pygame.transform.flip(self.image[self.frames-1], self.direccion, False), (self.rect.left-self.width_ajust//2, self.rect.top))