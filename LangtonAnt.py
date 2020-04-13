# 4 de Octubre de 2020
# Hormiga de Langton por Vladimir Alfaro
# Modelo 1 

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
AlVen = 450
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('Hormiga de Langton')
Ventana.fill(AzulC)

#----- Datos para la creacion del tablero ------
DimTablero = 402
(Xi,Yi) = (AnVen/2 - DimTablero/2, AlVen/2 - DimTablero/2) 
pygame.draw.rect(Ventana, gris, (Xi, Yi, DimTablero, DimTablero))
AltoCasilla = 6
AnchoCasilla = 6
Margen = 2

def Iterador(PosIni, AnchoCas, Marg, DimTab):
    i = 0
    n = PosIni
    a = AnchoCas + Marg
    b = int(DimTab/a)
    while i < b:
        yield n
        i = i + 1
        n = n + a

#print(*Iterador(Xi,AnchoCasilla,Margen,DimTablero))   #Iterador para las casillas en fila
#print(*Iterador(Yi,AltoCasilla,Margen,DimTablero))    #Iterador para las casillas en colunmas
#----- Final de los datos -----

#----- Dibujar Tablero cuadriculado: -----
for columna in Iterador(Xi,AnchoCasilla,Margen,DimTablero):
    for fila in Iterador(Yi,AltoCasilla,Margen,DimTablero):
        pygame.draw.rect(Ventana,blanco,(columna + Margen,fila + Margen, AnchoCasilla, AltoCasilla))
        #pygame.draw.rect(Ventana,gris,(columna, fila, Margen + AnchoCasilla, Margen))
        #pygame.draw.rect(Ventana,gris,(columna, fila + Margen, Margen, AltoCasilla))

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
    
    #Colocar hormigas:

    (Xm, Ym) = pygame.mouse.get_pos()
    #print(Xm , Ym)
    pygame.display.update()
