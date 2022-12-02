import pygame

class ProgressBar:
    def __init__(self, icon, length, divisions, screen):
        self.icon = icon
        self.icon_rect = self.icon.get_rect()
        self.bar_length = length
        self.bar_divisions = divisions
        self.bar_parts = 0
        self.bar_out = pygame.rect.Rect((0, 0, self.bar_length, self.icon_rect.height))
        self.screen = screen

    def draw_progress_bar(self, pos):
        self.icon_rect.midleft = pos
        self.screen.blit(self.icon, self.icon_rect)
        self.bar_out.midleft = self.icon_rect.midright
        pygame.draw.rect(self.screen, (236, 239, 241), self.bar_out, border_radius=20)
        padding = 3
        if self.bar_parts/self.bar_divisions < 0.33:
            color = (229, 57, 53)
        elif self.bar_parts/self.bar_divisions < 0.67:
            color = (253, 216, 53)
        elif self.bar_parts/self.bar_divisions < 1:
            color = (67, 160, 71)
        else:
            color = (3, 169, 244)
        bar_in = (self.bar_out.left+padding, self.bar_out.top+padding, int((self.bar_length-padding*2)/self.bar_divisions*self.bar_parts) ,self.bar_out.height-padding*2)
        pygame.draw.rect(self.screen, color, bar_in, border_radius=20)
        return (self.icon_rect.right+self.bar_length+15, self.icon_rect.centery)

    def add_part(self):
        self.bar_parts += 1