import pygame

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.image_base = pygame.transform.scale(image, (int(width * scale), int(height * scale)))#Imagen auxiliar para escribir texto sobre el boton
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = True
		#Superficie auxiliar para dibujar cuando el boton este desactivado
		self.btn_disabled = pygame.Surface((self.rect.width, self.rect.height)).convert_alpha()
		self.btn_disabled.fill((0, 0, 0, 200))

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
			surface.blit(self.btn_disabled, (self.rect.x, self.rect.y))
			return False

		#Draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		#Click
		return action

	def draw_text(self, text, color):
		type = pygame.font.SysFont("comic sans ms", self.rect.height // 10 * 5)
		textobj = type.render(text, True, color)
		textrect = textobj.get_rect()
		textrect.center = (self.rect.width//2, self.rect.height//2)
		self.image.blit(self.image_base, (0, 0))
		self.image.blit(textobj, textrect)