# Caracas, Venezuela.
# Fecha de inicio: 10/04/2020.
# Final: 21/04/2020
# Hormiga de Langton 
#Por Vladimir Alfaro
# Version 1.0

import pygame, sys, copy
from pygame.locals import *
from random import randint

pygame.init()

#----- Colores -----
blanco = pygame.Color(255,255,255)
negro = pygame.Color(0,0,0)
gris = pygame.Color(125,125,125)
AzulC = pygame.Color(26,196,178)
Vino = pygame.Color(66,19,23)

#----- Configuraciones de la ventana -----
AnVen = 800
AlVen = 450
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('Hormiga de Langton')
Ventana.fill(AzulC)

#----- Datos para la creacion del tablero ------
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

DimTablero = 400
(Xi,Yi) = (AnVen/2 - DimTablero/2, AlVen/2 - DimTablero/2) 
AltoCasilla = 6
AnchoCasilla = 6
Margen = 2
pygame.draw.rect(Ventana, gris, (Xi, Yi, DimTablero + Margen, DimTablero + Margen))

def Iterador(PosIni, AnchoCas, Marg, DimTab):         #Iterador para determinar las posiciones reales de las celdas que se van a dibujar
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

#----- Dibujar Tablero cuadriculado -----
for columna in Iterador(Xi,AnchoCasilla,Margen,DimTablero):
    for fila in Iterador(Yi,AltoCasilla,Margen,DimTablero):
        pygame.draw.rect(Ventana, negro, (columna + Margen,fila + Margen, AnchoCasilla, AltoCasilla))
        #pygame.draw.rect(Ventana,gris,(columna, fila, Margen + AnchoCasilla, Margen))
        #pygame.draw.rect(Ventana,gris,(columna, fila + Margen, Margen, AltoCasilla))

#----- Creacion de variables y matrices auxiliares -----
NumCel = int(DimTablero/(AltoCasilla + Margen))                                                 #Numero de celdas que puede haber dentro del tablero
MatColores = [[0 for x in range(NumCel)] for y in range(NumCel)]                                #Matriz de colores del tablero
MatHormigas = [[0 for x in range(NumCel)] for y in range(NumCel)]                               #Matriz de hormigas
MatAuxHormigas = [[0 for x in range(NumCel)] for y in range(NumCel)]                            #Matriz de hormigas auxiliar
MatDirecciones = [[[2 for x in range(4)] for x in range(NumCel)] for y in range(NumCel)]        #Matriz de direcciones de cada hormiga
MatAuxDirExtras = [[[0 for x in range(4)] for x in range(NumCel)] for y in range(NumCel)]       #Matriz para tener mas de una hormiga en cada celda
MatZeros =  [[0 for x in range(NumCel)] for y in range(NumCel)]                                 #Matriz completa de ceros
MatZeros1 =  [[[0 for x in range(4)] for x in range(NumCel)] for y in range(NumCel)]            #Matriz completa de ceros
Norte, Este, Sur, Oeste = 0, 1, 2, 3                                                            #Direcciones enumeradas

#----- Ubicacion de hormigas en el tablero -----
while True:
    for Evento in pygame.event.get():        
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit
        if Evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, 0, 0):
                (Xm, Ym) = pygame.mouse.get_pos()
                if(Xi <= Xm < Xi + DimTablero and Yi <= Ym < Yi + DimTablero):
                    Xnew = int((Xm-Xi)/(AnchoCasilla + Margen))
                    Ynew = int((Ym-Yi)/(AltoCasilla + Margen))
                    MatHormigas[Ynew][Xnew] = 1
                    print((Ynew,Xnew))
    if Evento.type == pygame.KEYDOWN:
        if Evento.key == K_KP_ENTER or Evento.key == K_SPACE:
            break
    pygame.display.update()

#print(MatHormigas)
#print(MatDirecciones)
cont = 0

while True:                                                             #Loop infinito para mantener abierta la ventana
    
    Reloj = pygame.time.Clock()                                         #Reloj funcionando a 1 cuadro por segundo
    Reloj.tick(5)
    #----- Intrucciones del automata-----
    i, j = 0, 0
    while i < NumCel - 1:
        while j < NumCel -1:
            if MatHormigas[i][j] > 0:
                l = MatHormigas[i][j]                                   #Puede valer 0, 1, 2, 3 o 4   
                if MatColores[i][j] == 0:
                    MatColores[i][j] = 1
                    #Aqui deberia pintar los cuadros de blanco
                    pygame.draw.rect(Ventana, blanco, (j*(AltoCasilla + Margen) + Xi + Margen, i*(AnchoCasilla + Margen) + Yi + Margen, AnchoCasilla, AltoCasilla))
                    #print((j*(AltoCasilla + Margen) + Xi + Margen, i*(AnchoCasilla + Margen) + Yi + Margen))
                    while l > 0:
                        l = l - 1
                        if MatDirecciones[i][j][l] == 0:
                            MatDirecciones[i][j][l] = 0 
                            k = MatAuxHormigas[i][j + 1]
                            MatAuxDirExtras[i][j + 1][k] = 1
                            MatAuxHormigas[i][j + 1] = MatAuxHormigas[i][j + 1] + 1

                        elif MatDirecciones[i][j][l] == 1:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i + 1][j]
                            MatAuxDirExtras[i + 1][j][k] = 2
                            MatAuxHormigas[i + 1][j] = MatAuxHormigas[i + 1][j] + 1

                        elif MatDirecciones[i][j][l] == 2:
                            MatDirecciones[i][j][l] = 0    
                            k = MatAuxHormigas[i][j - 1]
                            MatAuxDirExtras[i][j - 1][k] = 3
                            MatAuxHormigas[i][j - 1] = MatAuxHormigas[i][j - 1] + 1

                        elif MatDirecciones[i][j][l] == 3:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i - 1][j]
                            MatAuxDirExtras[i - 1][j][k] = 0
                            MatAuxHormigas[i - 1][j] = MatAuxHormigas[i - 1][j] + 1         
                    j = j + 1
                elif MatColores[i][j] == 1:
                    MatColores[i][j] = 0
                    #Aqui deberia pintar los cuadros de negro
                    pygame.draw.rect(Ventana, negro, (j*(AltoCasilla + Margen) + Xi + Margen, i*(AnchoCasilla + Margen) + Yi + Margen, AnchoCasilla, AltoCasilla))
                    #print((j*(AltoCasilla + Margen) + Xi + Margen, i*(AnchoCasilla + Margen) + Yi + Margen))
                    while l > 0:
                        l = l - 1
                        if MatDirecciones[i][j][l] == 0:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i][j - 1]
                            MatAuxDirExtras[i][j - 1][k] = 3
                            MatAuxHormigas[i][j - 1] = MatAuxHormigas[i][j - 1] + 1
                        
                        elif MatDirecciones[i][j][l] == 1:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i - 1][j]
                            MatAuxDirExtras[i - 1][j][k] = 0
                            MatAuxHormigas[i - 1][j] = MatAuxHormigas[i - 1][j] + 1

                        elif MatDirecciones[i][j][l] == 2:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i][j + 1]
                            MatAuxDirExtras[i][j + 1][k] = 1
                            MatAuxHormigas[i][j + 1] = MatAuxHormigas[i][j + 1] + 1
                        
                        elif MatDirecciones[i][j][l] == 3:
                            MatDirecciones[i][j][l] = 0
                            k = MatAuxHormigas[i + 1][j]
                            MatAuxDirExtras[i + 1][j][k] = 2
                            MatAuxHormigas[i + 1][j] = MatAuxHormigas[i + 1][j] + 1
                    j = j + 1    
            else: 
                j = j + 1
        j = 0 
        i = i + 1          
    cont = cont + 1
    MatHormigas = copy.deepcopy(MatAuxHormigas)    
    MatDirecciones = copy.deepcopy(MatAuxDirExtras)
    #print(cont)
    #print(MatHormigas)   
    #print(MatDirecciones)
    #print(MatColores)
    MatAuxHormigas = copy.deepcopy(MatZeros)
    MatAuxDirExtras = copy.deepcopy(MatZeros1)
    
    for Evento in pygame.event.get():                                   #Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
