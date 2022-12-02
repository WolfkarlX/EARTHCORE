import pygame 

class Item(pygame.sprite.Sprite):
	def __init__(self,pos,size, img_dir, id, replacement = ()):
		super().__init__()
		self.image = pygame.image.load(img_dir).convert_alpha()
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect(topleft = pos)
		self.type_item = id
		self.replacement = replacement