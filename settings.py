####Tamaño de la ventana
WIDTH_SCREEN = 900

####Colores basicos
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

####Lenguaje
language = "english"

play_btn_text = {"english" : "Play", "spanish" : "Jugar"}

set_language_text = {"english" : "English", "spanish" : "Español"}

level_1_btn_text = {"english" : "Level 1", "spanish" : "Nivel 1"}
level_2_btn_text = {"english" : "Level 2", "spanish" : "Nivel 2"}
level_3_btn_text = {"english" : "Level 3", "spanish" : "Nivel 3"}

###Niveles del juego
level_map_1 = [
'                    ',
'                    ',
'          XXXX      ',
'             XX     ',
'                    ',
'                XXXX',
'      X             ',
'     XX       XXXXXX',
'XXXXXXXXXXXXXXXXXXXX',
]
tile_size = 50
HEIGHT_SCREEN = len(level_map_1) * tile_size

background_level_1 = "images/backgrounds/fondo_nivel1.png"
tile_level_1 = "images/tiles/bloque_nivel1.png"
frames_human = []

frames_hongy = ["images/humano/Personaje by like1.png", "images/humano/Personaje1.png", "images/humano/Personaje2.png", "images/humano/Personaje3.png", "images/humano/Personaje4.png", "images/humano/Personaje saltando .png"]