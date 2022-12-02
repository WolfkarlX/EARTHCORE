import pygame

class Enemy:
    def __init__(self, image_dir, dim, pos_ini, route):
        self.image = []
        self.frames = 0
        for id, img in enumerate(image_dir):
            self.image.append(pygame.image.load(img).convert_alpha())
            self.frames += 1
        for id, img in enumerate(self.image):
            self.image[id] = pygame.transform.scale(img, dim)
        self.rect = self.image[0].get_rect(topleft=pos_ini)

        self.frame_actual = 0
        self.frame_count = 0

        self.vel_x = 1

        self.direccion = True
        self.pos_ini = list(pos_ini)
        self.route = route

    def dibujar(self, screen):
        self.frame_count += 1
        if self.frame_count > 6:
            self.frame_actual += 1
            self.frame_count = 0
            if self.frame_actual >= self.frames:
                self.frame_actual = 0

        if self.route != 0:
            if self.direccion:
                self.rect.x += self.vel_x
                if self.rect.right >= self.pos_ini[0] + self.route:
                    self.direccion = False
            else:
                self.rect.x -= self.vel_x
                if self.rect.left <= self.pos_ini[0]:
                    self.direccion = True

        screen.blit(pygame.transform.flip(self.image[self.frame_actual], self.direccion, False), self.rect)
                                                          