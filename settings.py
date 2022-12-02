from os import path
origin_dir = path.dirname(__file__)
####Tamaño de la ventana
WIDTH_SCREEN = 1200
####Colores basicos
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

####Lenguaje
language = "english"

play_btn_text = {"english" : "Play", "spanish" : "Jugar"}

set_language_text = {"english" : "English", "spanish" : "Español"}
label_language_text = {"english" : "Language:", "spanish" : "Idioma:"}
set_mode_text = {"english" : {"easy": "Easy", "hard": "Hard"}, "spanish" : {"easy": "Fácil", "hard": "Difícil"}}
label_mode_text = {"english" : "Mode:", "spanish" : "Dificultad:"}
label_music_text = {"english" : "Music:", "spanish" : "Música:"}

level_1_btn_text = {"english" : "Level 1", "spanish" : "Nivel 1"}
level_2_btn_text = {"english" : "Level 2", "spanish" : "Nivel 2"}
level_3_btn_text = {"english" : "Level 3", "spanish" : "Nivel 3"}

level_pause_text = {"english" : "Pause", "spanish" : "Pausa"}
press_Q_text = {"english" : "Press Q to exit", "spanish" : "Presiona Q para salir"}
press_R_text = {"english" : "Press R to return", "spanish" : "Presiona R para regresar"}

level_GAME_OVER_text = {"english" : "GAME OVER", "spanish" : "FIN DEL JUEGO"}
press_ESC_text = {"english" : "Press ESCAPE To Exit", "spanish" : "Presiona ESCAPE para salir"}
level_completed_text = {"english" : "IT´S TIME TO CONTINUE!", "spanish" : "¡ES HORA DE CONTINUAR!"}
level_completed_text1 = {"english" : "the seeds have been received.....", "spanish" : "Las semillas han sido recibidas....."}
level_completed_text2 = {"english" : "Press SPACE to continue", "spanish" : "Presiona ESPACIO para continuar"}
level_completed_text3 = {"english" : "CONGRATULATIONS!", "spanish" : "¡FELICIDADES!"}
level_completed_text4 = {"english" : "You saved the ecosystem!", "spanish" : "¡Salvaste el ecosistema!"}

objetive_level_1_text = {"english" : "MISSION: Collect the seeds & trash bags", "spanish" : "OBJETIVO: Recolecta las semillas y las bolsas de basura"}
objetive_level_2_text = {"english" : "MISSION: Plant the seeds", "spanish" : "OBJETIVO: Planta las semillas"}
objetive_level_3_text = {"english" : "MISSION: Water the plants", "spanish" : "OBJETIVO: Riega las plantas"}

Pause_txt = {"english":"Key P = Pause", "spanish":"Tecla P = pausa"}

###Niveles del juego
level_map_1 = [                                                                                                                                                                                                                                                         
'I                                                                                                                                                                                                                                                              I',    
'I                                                                                                                                                                                                                                                              I',
'I                                                                                                                                                                                                                                                              I',
'I                                                                                                                                                                                                                              XXXXXXXXXXXX       XXXXXXXXXX 1 I',
'I         1Y           1          1Y                         1Y         1                                                              XXXXXXXXXXXXX      1                                                                   XU                 X           1 I',
'I         XXXX        XX    XXXXXXXXX                 XXXXXXXXXXX     XXXXX   XXXXX                                  XXXXX            XUUUUUUUUUUUUUXXXXXXXXXXXXXXX                                                XXXXXXXXXXXU                              1 I',
'I            UX1            UUUUUUUUUX                UUUUUUUUUUUX1                        XXXXXXXXXXXX   XXXXXXXXXXXU                                            UX                                                                                         1 I',
'I             UXX    X1        UUUUUUUX                          UX                       XUUUUUUUUUUUU                       XXXX                                 UXX                                      XXX                    XXXX    XXXXXXXXX         1 I',
'I     T              UXXX      UUUUUUUUXXXXX                            XXXX                          UX                                                                                            XXXXXXXX                                                 1 I',
'I     X            1       Y   U                                      1     2   Y                   2 UUX                                           2Y                   XXXX                                                                         X      1 I',
'I1 Y  UX1  T  2XXXXXXXXXXXXXXXXU1                    1     1     2XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXUUU   1       XXXXXXX     1      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUX                                                      X    X    X              1 I',                                                                                                                                                              
'IXXXXXUUXXXXXXXUUUUUUUUUUUUUUUUUXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXUUUUUUUUUUUUUUUUUXX  UUUUUUUUUUUUUUUUUUXXXXXXXXXXXUUUUUUU   XXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXUXXXXUXXXXUXXXXXXXXXXX   X X',
]

level_map_2 = [
'I                                                                                                                                                                                                                                                              I',
'I                                                                                                                                                                                                                                                              I',
'I                                                                                         1                                                                                                                 1                                                  I',
'I                                                                                        XX                                                                                                                XX                                          XXX     I',
'I                                                                                       1U                                                                           XXXXXXXXXXXXXXXX                     1U                           1          1            I',
'I                            1                                        X       X        XXU               1                                                          XU                  X       X        XXU               1           XXXXX   XXXXXXX         I',
'I       1     Y 1          XXXXXXX     1                             XU    1       Y          1      XXXXXXX                                                                           XU    1       Y          1      XXXXXXX                                 I',
'I      XXXXXXXXXXXX    XXXXUUUUUUU     XXXX                     X   XU   XXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXX                           XXXXXXXXXXXXXXXXXX                   XU   XXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXX                       I',
'I                    XXUUUUUUUU  UX   1                        XU                                  U           UUUUUUUX                      XXXXU                U              XXXX                                                  UX                      I',
'I                  1XUUUUUUUU         X                     XX                                     UX                                     XXXU                    UX          XX                                                             XXXX              I',
'I        1     1XXXXUUUUUUUUUXX1              Y     Y                    Y    1     Y                       1        1                                      1     UUX                           1     Y                       1                        1       I',          
'IXXXXXXXXXXXXXXXUUUUUUUUUUUUUUUXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXI',
]

level_map_3 = [
'I                                                                                                                                                                                                                                                                                                                                                                                       I',   
'I                                                                                                                                                                                                                                                Z                                                                                                                                      I',
'I                                                                                                                                                                                                                                         XXX   XXXX    X                                                                                                        1                      I',
'I                                                                                               1Z                                                                                                                                                     XUXXXXXXXX                                                                                               XXX                     I',
'I                                                                                              XXX                                                                                            1      1      TY     1           TY     1               XUUUUUUUUUUX                                                                   X                 Z      XXUUUXX                   I',
'I                                                                                            X                                                                     Z                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXUUUUUUUUUUUUX                                             XX  XXX      1     TY   Z    1       XXXXXXX                 1          I',
'I                         TY                 Z1                                             X                         1                         Z          XX  X  XXX                XXX  UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU        XUUUUUUUUUUUUUUUU                                         XX           XXXXXXXXXXXXXXXXXXXXXXXXXX                    XXXXXXXXXXX      I',
'I                        XXXXX               XXX                                      1    X                         XXX  X  Z                 XXXX   XXX                     X  XX                                                               UUU        UUUUUUX                                    XX                                                                        X     I',
'I                       XUUUUUX                   1                         Z 1   XX XXX        1Z                          XX       1     XXX                                U                                                                XXXUUU        UUUUUUUX                                XXXUU                                                                         XX   I',
'I                      XUUUUUUUX                XXXXX                       XXXXX             XXXX            XXX               XXXXXXXXXX                                   XU                                                               XUUUUUU        UUUUUUUUX                             XXUUUUU                                                                             XI',
'IZ  1     1  ZTY      XUUUUUUUUUX  1  TY    1  Z      1       1       1                    XXXUUUU   1        UUUXTY   1        UUUUUUUUUU  Z       1    Z    TY    1          Z      1         Z      1                Z            1      XXUUUUUUUX Z 1                TY       1         Z            TY      1     TY       1       TY         1       TY      1              1   ZI',
'IXXXXXXXXXXXXXXXXXXXXXUUUUUUUUUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUUUUXXXXXXX   XXUUUUXXXXXXXXXXXXXXUUUUUUUUUUXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXUUUUUUUUUUUUUUUUUUUUUUUUUUXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXI',
]


tile_size = 50
HEIGHT_SCREEN = len(level_map_1) * tile_size

#Items
item_seed = "images/items/item_semilla.png"
item_trash = "images/items/item_basura.png"
item_sprout = "images/items/item_retoño.png"
item_mound = "images/items/monton_tierra.png"
item_back_Tree = "images/items/item_tree.png"
item_back_dryTree = "images/backgrounds/árbol_seco.png"
item_back_warning = "/images/items/Peligro.png"
item_back_foxUwU = "/images/items/zorro.png"

###Interfaz comun de los niveles
difficulty = 'easy'
Timer_img = "images/interface/reloj.png"
time_pass_level = {'easy' : 480, 'hard' : 240} #Tiempo para pasar el nivel, 

tile_invisible = "images/tiles/invisible.png"
dead_sound_effect = origin_dir + "/sound/effects/Muerte.wav"
jump_sound = origin_dir + "/sound/effects/Jump_Sound.wav"

###Propiedades de nivel
open_level_1 = True
background_level_1 = "images/backgrounds/fondo_nivel1.png"
tile_grass_level_1 = "images/tiles/bloque_nivel1.png"
tile_dirt_level_1 = "images/tiles/bloque_tierra_nivel1.png"
items_level_1 = ((item_seed, (26, 26), item_seed), (item_trash, (50, 50), item_trash))
item_sound_effect_level_1 = origin_dir + "/sound/effects/basura3.wav"
item_back_level_1 = ((item_back_dryTree, (80, 120), "T"), )

frames_human = ["images/human/Personaje1.png", "images/human/Personaje2.png", "images/human/Personaje3.png", "images/human/Personaje4.png", "images/human/Personaje5.png"]
for index, frame in enumerate(frames_human):
    frames_human[index] = origin_dir + "/" + frame
character_level_1 = (frames_human, 40, 63, (300, 235), -20, 14)#Frames, dimensiones, posicion incial en la ventana, fuerza del salto, ajuste de anchura

frames_enemy_1 = ["images/enemies/Evil1.png", "images/enemies/Evil2.png", "images/enemies/Evil3.png", "images/enemies/Evil4.png"]
enemy_level_1 = [frames_enemy_1, (44, 72), 100]


open_level_2 = True
background_level_2 = "images/backgrounds/fondo_nivel2.png"
tile_grass_level_2 = "images/tiles/bloque_nivel2.png"
tile_dirt_level_2 = "images/tiles/bloque_tierra_nivel2.png"
items_level_2 = ((item_mound, (36, 14), item_sprout, (52, 40)), )
item_sound_effect_level_2 = origin_dir + "/sound/effects/germinar.wav"


frames_hongy = ["images/hongy/HongyEstaticoHD1.png", "images/hongy/HongyEstaticoHD1.png", "images/hongy/HongyEstaticoHD3.png", "images/hongy/HongyEstaticoHD4.png", "images/hongy/HongyEstaticoHD5.png", "images/hongy/HongyEstaticoHD6.png", "images/hongy/HongySalto.png"]
for index, frame in enumerate(frames_hongy):
    frames_hongy[index] = origin_dir + "/" + frame
character_level_2 = (frames_hongy, 30, 30, (300, 250), -17, 0)


enemy_level_2 = [frames_enemy_1, (44, 72), 100]


open_level_3 = True
background_level_3 = "/images/backgrounds/fondo_nivel3.png"
tile_grass_level_3 = "images/tiles/bloque_nivel3.png"
tile_dirt_level_3 = "/images/tiles/bloque_pura_tierra_nivel3.png"
items_level_3 = ((item_sprout, (52, 40), item_back_Tree, (150, 180)), )
item_sound_effect_level_3 = origin_dir + "/sound/effects/agua_sonido.wav"
item_back_level_3 = ((item_back_warning, (54, 70), "T"), (item_back_foxUwU, (47, 44), "Z"))

frames_hongy_shower = ["images/hongy/HongyShower1.png", "images/hongy/HongyShower2.png", "images/hongy/HongyShower3.png", "images/hongy/HongyShower4.png", "images/hongy/HongyShower5.png", "images/hongy/HongyShower6.png", "images/hongy/HongyShower7.png"]
for index, frame in enumerate(frames_hongy_shower):
    frames_hongy_shower[index] = origin_dir + "/" + frame
character_level_3 = (frames_hongy_shower, 36, 42, (300, 250), -17, 2)

frames_enemy_3 = ["images/enemies/Arbusto.png"]
enemy_level_3 = [frames_enemy_3, (74, 36), 0]

#Estados 
start = "start"
config = "config"
level_selector = "level_selector"
level_1 = "level_1"
level_2 = "level_2"
level_3 = "level_3"
controls = "controls"
lore = "lore"
lore1 = "lore1"
pause = "pause"


background_controls_img = "/images/backgrounds/fondo_config.png"
hongy1 = "/images/hongy/Hongy Llorando1.png"
hongy2 = "/images/hongy/Hongy Llorando2.png"
hongy3 = "/images/hongy/Hongy Llorando3.png"
hongy4 = "/images/hongy/Hongy Llorando4.png"
hongy5 = "/images/hongy/Hongy Llorando5.png"
hongy6 = "/images/hongy/Hongy Llorando6.png"



control_button_btn = "/images/buttons/controles_boton.png"
background_level_1_finished = "/images/backgrounds/Fondo_Dar.png"
background_level_2_finished = "/images/backgrounds/BosqueHD.jpeg"
background_level_3_finished = "/images/final/final.png"
background_controls_img = "/images/backgrounds/Fondo Controles.png"








