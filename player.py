import pygame

class Player():
    def __init__(self, image_dir, width, height, pos):
        self.image = []
        self.frames = 0
        for id, img in enumerate(image_dir):
            self.image.append(pygame.image.load(img).convert_alpha())
            self.frames += 1
        for id, img in enumerate(self.image):
            self.image[id] = pygame.transform.scale(img, (width, height))
        self.rect = self.image[0].get_rect(topleft= pos)

        self.player_jump = -15
        self.caminando = False
        self.en_tierra = False
        self.direccion = True
        self.gravedad = 7
        
        self.frame_actual = 0
        self.frame_count = 0

        self.vel_x = 0
        self.vel_y = 0
        self.vel = 6

    def eventos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.en_tierra == True:
                self.vel_y = self.player_jump
                self.en_tierra = False
            if event.key == pygame.K_a:
                self.direccion = False
                self.caminando = True
                self.vel_x = -self.vel
            if event.key == pygame.K_d:
                self.direccion = True
                self.caminando = True
                self.vel_x = self.vel
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.vel_x = 0
                self.frame_actual = 0
                self.caminando = False
            if event.key == pygame.K_d:
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
        if self.caminando:
            self.frame_count += 1
            if self.frame_count > 5:
                self.frame_actual += 1
                self.frame_count = 0
                if self.frame_actual >= self.frames:
                    self.frame_actual = 0
            screen.blit(pygame.transform.flip(self.image[self.frame_actual], self.direccion, False), self.rect)
        else:
            screen.blit(pygame.transform.flip(self.image[0], self.direccion, False), self.rect)