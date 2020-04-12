# 4 de Octubre de 2020
# Hormiga de Langton por Vladimir Alfaro
# Modelo 1 

import pygame, sys
from pygame.locals import *

color1 = (20, 0, 50)  #Morado // Tener cuidado porque es un elemento de tipo tupla y no tipo color
color2 = pygame.Color(255,255,255)  #Naranja // Este si es tipo color

pygame.init()                           # A partir de esta linea funcionaran todas las instrucciones de pygame

Ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('Ventana para la hormiga de Langton')
Ventana.fill(color1)
pygame.draw.line(Ventana,color2,(60,80), (160,100), 4)  #pygame.draw.line(donde estara la linea, color de la linea, (xi,yi), (xf,yf), ancho de la linea )

print(color2.r)      #Como extraer la saturacion roja de un color
print(color2.g)      #Como extraer la saturacion verde de un color
print(color2.b)      #Como extraer la saturacion azul de un color

while True:                             # Loop infinito para mantener abierta la ventana

    for Evento in pygame.event.get():       # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
