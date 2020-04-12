# 4 de Octubre de 2020
# Hormiga de Langton por Vladimir Alfaro
# Modelo 1 

import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()                           # A partir de esta linea funcionaran todas las instrucciones de pygame

color1 = pygame.Color(128,64,0)     #Madera
color2 = pygame.Color(34,113,179)   #Azul claro
color3 = pygame.Color(155,155,155)  #Gris
AnVen = 700
AlVen = 400
AnTab = 300
AlTab = 300
(Xi,Yi) = (AnVen/2 - AnTab/2, AlVen/2 - AlTab/2)
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('Hormiga de Langton')
Ventana.fill(color1)

pygame.draw.rect(Ventana,color3,(Xi,Yi, AnTab,AlTab))  #tablero de 200x200 pixeles
pygame.draw.line(Ventana, color2, (Xi-2,Yi-2), (Xi+AnTab+2,Yi-2), 4)
pygame.draw.line(Ventana, color2, (Xi+AnTab+2,Yi-2), (Xi+AnTab+2,Yi+AlTab+2), 4)
pygame.draw.line(Ventana, color2, (Xi+AnTab+2,Yi+AlTab+2), (Xi-2,Yi+AlTab+2) , 4)
pygame.draw.line(Ventana, color2, (Xi-2,Yi+AlTab+2), (Xi-2,Yi-2) , 4)

"""
#-----Solicitud de Dimensiones del tablero-----
while True:
    try:
        Dimension = int(input('Por favor ingresa la dimension de tu tablero: '))
        break
    except(TypeError, ValueError):
        print('Hey! Eso no es un numero.\nIntentalo otra vez.')
#-----Final de la solicitud-----
"""


while True:                             # Loop infinito para mantener abierta la ventana
    for Evento in pygame.event.get():       # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
