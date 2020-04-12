# 4 de Octubre de 2020
# Hormiga de Langton por Vladimir Alfaro
# Modelo 1 

import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()                           # A partir de esta linea funcionaran todas las instrucciones de pygame

#-----Colores-----
blanco = pygame.Color(255,255,255)
negro = pygame.Color(0,0,0)
color1 = pygame.Color(128,64,0)     #Madera
#-----

AnVen = 700
AlVen = 700
AnTab = 300
AlTab = 300
(Xi,Yi) = (AnVen/2 - AnTab/2, AlVen/2 - AlTab/2)
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('Hormiga de Langton')
Ventana.fill(color1)

#-----Datos para la creacion del tablero -----
DimTablero = 400 
AltoCasilla = 10
AnchoCasilla = 10
Margen = 5

def Iterador(AnchoCas, Marg, DimVent):
    i = 0
    n = 0
    a = AnchoCas + Marg
    while n < DimVent:
        yield n
        i += 1
        n = i*a
#----- Final de los datos -----

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
    
    #Dibujar Tablero cuadriculado:
    for columna in Iterador(AnchoCasilla,Margen,DimTablero):
        for fila in Iterador(AnchoCasilla,Margen,DimTablero):
            pygame.draw.rect(Ventana,negro,(columna,fila + Margen,Margen,AltoCasilla))
            pygame.draw.rect(Ventana,blanco,(columna + Margen,fila + Margen, AnchoCasilla, AltoCasilla))
    #-------
    
    
    pygame.display.update()
