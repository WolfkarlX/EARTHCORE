import pygame 

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size, img_dir):
		super().__init__()
		self.image = pygame.image.load(img_dir)
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)