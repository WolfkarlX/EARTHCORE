import pygame

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.image_base = pygame.transform.scale(image, (int(width * scale), int(height * scale)))#Imagen auxiliar
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = True

	def draw(self, surface, text="", reaction = True):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked = True
				action = True

		#check mouse is clicked
		if pygame.mouse.get_pressed()[0]:
			self.clicked = True
		else:
			self.clicked = False

		#draw optional text
		if text:
			self.draw_text(text, (0, 0, 0))

		#Option disabled button
		if not reaction:
			self.image.fill((0, 0, 0, 200))

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		if reaction:
			return action
		else:
			False

	def draw_text(self, text, color):
		type = pygame.font.SysFont("comicsanssms", self.rect.height // 10 * 7)
		textobj = type.render(text, True, color)
		textrect = textobj.get_rect()
		textrect.center = (self.rect.width//2, self.rect.height//2)
		self.image.blit(self.image_base, (0, 0))
		self.image.blit(textobj, textrect)