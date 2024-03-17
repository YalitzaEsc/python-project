import pygame
import random

# Inicializar a pygame
pygame.init()

# Primero alto luego ancho, para crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasión Gatuna")
icono = pygame.image.load('catDos.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Jugador
img_jugador = pygame.image.load('catDos.png')
# Posiciones jugador
jugador_x = 368
jugador_y = 536
jugador_movimiento_x = 0

# Enemigo
img_enemigo = pygame.image.load('happy.png')
# Posiciones enemigo
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_movimiento_x = 3
enemigo_movimiento_y = 50


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# Loope del juego para que no se cierra la pantalla
se_ejecuta = True
while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # iterar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador_movimiento_x = 3
            if evento.key == pygame.K_LEFT:
                jugador_movimiento_x = -3

        # Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_movimiento_x = 0

    # Actualizar ubicación del jugador
    jugador_x += jugador_movimiento_x

    # Actualizar ubicación del enemigo
    enemigo_x += enemigo_movimiento_x

    # Limitar bordes del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Limitar bordes del enemigo
    if enemigo_x <= 0:
        enemigo_movimiento_x = 3
        enemigo_y += enemigo_movimiento_y
    elif enemigo_x >= 736:
        enemigo_movimiento_x = -3
        enemigo_y += enemigo_movimiento_y

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar pantalla
    pygame.display.update()
