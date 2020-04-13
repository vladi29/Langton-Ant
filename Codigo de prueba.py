import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()                           # A partir de esta linea funcionaran todas las instrucciones de pygame

#----- Colores -----
blanco = pygame.Color(255,255,255)
negro = pygame.Color(0,0,0)
gris = pygame.Color(125,125,125)
AzulC = pygame.Color(26,196,178)

#----- Ventana -----
AnVen = 800
AlVen = 500
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('Hormiga de Langton')
Ventana.fill(AzulC)

#----- Areglo de pixeles ----- 

Surf = pygame.Surface((8,8))
CeldaViva = Surf.fill(blanco)
CeldaMuerta = Surf.fill(negro)

Surf.set_at((50, 50), blanco)

while True:                             # Loop infinito para mantener abierta la ventana
    
    for Evento in pygame.event.get():       # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit
    
    pygame.display.update()