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

#----- Datos para la creacion del tablero ------
DimTablero = 400
(Xi,Yi) = (AnVen/2 - DimTablero/2, AlVen/2 - DimTablero/2) 
AltoCasilla = 6
AnchoCasilla = 6
Margen = 2
pygame.draw.rect(Ventana, gris, (Xi, Yi, DimTablero + Margen, DimTablero + Margen))

def Iterador(PosIni, AnchoCas, Marg, DimTab):
    i = 0
    n = PosIni
    a = AnchoCas + Marg
    b = int(DimTab/a)
    while i < b:
        yield n
        i = i + 1
        n = n + a

for columna in Iterador(Xi,AnchoCasilla,Margen,DimTablero):
    for fila in Iterador(Yi,AltoCasilla,Margen,DimTablero):
        pygame.draw.rect(Ventana,blanco,(columna + Margen,fila + Margen, AnchoCasilla, AltoCasilla))
#----- Arreglo de pixeles ----- 

NumCel = int(DimTablero/(AltoCasilla + Margen))
MatColores = [[0 for x in range(NumCel)] for y in range(NumCel)]
MatHormigas = [[0 for x in range(NumCel)] for y in range(NumCel)]
Norte, Sur, Este, Oeste = 0, 1, 2, 3
Dir = Norte

#print(MatAux)

while True:                             # Loop infinito para mantener abierta la ventana
    
    for Evento in pygame.event.get():       # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit
        elif Evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, 0, 0):
                (Xm, Ym) = pygame.mouse.get_pos()
                if(Xi <= Xm < Xi + DimTablero and Yi <= Ym < Yi + DimTablero):
                    Xnew = int((Xm-Xi)/(AnchoCasilla + Margen))
                    Ynew = int((Ym-Yi)/(AltoCasilla + Margen)) 
                    #print(Ynew, Xnew)
                    #print('Estas dentro del tablero')
                    MatHormigas[Ynew][Xnew] = 1
                    print(MatHormigas) 
    # ----- instrucciones del Automata -----
        elif Evento.type == pygame.KEYDOWN:
            i, j = 0, 0
            while i <= NumCel:
                while j <= NumCel:
                    if MatHormigas[i][j] == 1:
                        MatHormigas[i][j] = 0
                        if MatColores[i][j] == 0:
                            MatColores[i][j] == 1
                            if Dir == Norte:
                                Dir = Este
                                MatHormigas[i][j+1] = 1
                            elif Dir == Este:
                                Dir = Sur
                                MatHormigas[i+1][j]
                            elif Dir == Sur:
                                Dir == Oeste
                                MatHormigas[i][j-1]
                            elif Dir == Oeste:
                                Dir = Norte
                                MatHormigas[i-1][j]
                            j = j + 1
                        elif MatColores[i][j] == 1:
                            MatColores[i][j] == 0
                            if Dir == Norte:
                                Dir = Este
                                MatHormigas[i][j+1] = 1
                            elif Dir == Este:
                                Dir = Sur
                                MatHormigas[i+1][j]
                            elif Dir == Sur:
                                Dir == Oeste
                                MatHormigas[i][j-1]
                            elif Dir == Oeste:
                                Dir = Norte
                                MatHormigas[i-1][j]
                            j = j + 1
                i = i + 1
                    
            print(MatColores)
            print(MatHormigas)                    
    pygame.display.update()
