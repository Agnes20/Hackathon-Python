import pygame, random

screent_width = 1280
screent_height = 960

#colors
white_color= (200,200,200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screent_width, screent_height))

def mover_rectangulo():
    global spped #permite acceder funciones de fuera
    if rectangulo.top + 50 < screent_height:
        rectangulo.top += spped

def start_bola():
    global spped_bola_x #permite acceder funciones de fuera
    global spped_bola_y #permite acceder funciones de fuera
    if bola.left + 50 > screent_width or bola.top <0:
        bola.top = screent_height // 2
        bola.left = screent_width // 2
    spped_bola_x = 3*random.choice((1,-1))
    spped_bola_y = 3*random.choice((1,-1))


def mover_bola():
    global spped_bola_x #permite acceder funciones de fuera
    global spped_bola_y #permite acceder funciones de fuera
    if bola.top + 50 > screent_height or bola.top <0:
        spped_bola_x = -spped_bola_x

    if bola.left < 10 and rectangulo.top < bola.top >rectangulo.top +140:
        spped_bola_y = -spped_bola_y

    start_bola()

    bola.top += spped_bola_x
    bola.left+= spped_bola_y


rectangulo = pygame.Rect(10,10,10,140)
bola = pygame.Rect(50,10,50,50)
spped = 0
spped_bola_x = 3
spped_bola_y = 3
while True:
    screen.fill(light_gray)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                spped = -3
            elif event.hey == pygame.K_DOWN:
                spped = 3
            elif event.hey == pygame.KEYUP:
                spped = 0

    mover_rectangulo()
    mover_bola()
    #dibujar
    pygame.draw.rect(screen,white_color, rectangulo)
    #dibujar
    pygame.draw.ellipse(screen,white_color, bola)
    pygame.display.flip() #refescar pantalla
    clock.tick(60)#calcula tick 60 frame por segundo
print("Kata4")