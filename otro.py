import pygame
import copy
from pygame.locals import *

pygame.init()

AnVen = 800
AlVen = 450
Ventana = pygame.display.set_mode((AnVen,AlVen))
pygame.display.set_caption('otro')
Ventana.fill((26,196,178))

DimTablero = 50
#(Xi,Yi) = (AnVen/2 - DimTablero/2, AlVen/2 - DimTablero/2) 
AltoCasilla = 4
AnchoCasilla = 4
Margen = 1

NumCel = int(DimTablero/(AltoCasilla + Margen))
MatColores = [[0 for x in range(NumCel)] for y in range(NumCel)]
MatHormigas = [[0 for x in range(NumCel)] for y in range(NumCel)]
MatAuxHormigas = [[0 for x in range(NumCel)] for y in range(NumCel)]
MatDirecciones = [[2 for x in range(NumCel)] for y in range(NumCel)] 
MatAuxDirecciones = [[0 for x in range(NumCel)] for y in range(NumCel)]
MatZeros =  [[0 for x in range(NumCel)] for y in range(NumCel)]
Norte, Este, Sur, Oeste = 0, 1, 2, 3


MatHormigas[5][4] = 1
#MatDirecciones[5][4] = 2

MatHormigas[5][5] = 1
#MatDirecciones[5][5] = 2

MatHormigas[5][6] = 1
#MatDirecciones[5][6] = 2

MatHormigas[5][7] = 1
#MatDirecciones[5][7] = 2

print(MatHormigas)
#print(MatDirecciones)
#print(MatColores)

aux = 0
while True:
    for Evento in pygame.event.get():        # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit
    
    reloj = pygame.time.Clock()
    reloj.tick(2)
    i, j = 0, 0
    while i < NumCel - 1:
        while j < NumCel -1:
            if MatHormigas[i][j] == 1:
                MatHormigas[i][j] = 0       
                if MatColores[i][j] == 0:
                    MatColores[i][j] = 1
                    if MatDirecciones[i][j] == 0:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i][j + 1] = 1
                        MatAuxHormigas[i][j + 1] = 1
                        j = j + 1
                    elif MatDirecciones[i][j] == 1:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i + 1][j] = 2
                        MatAuxHormigas[i + 1][j] = 1
                        j = j + 1
                    elif MatDirecciones[i][j] == 2:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i][j - 1] = 3
                        MatAuxHormigas[i][j - 1] = 1
                        j = j + 1 
                    elif MatDirecciones[i][j] == 3:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i - 1][j] = 0
                        MatAuxHormigas[i - 1][j] = 1
                        j = j + 1
                elif MatColores[i][j] == 1:
                    MatColores[i][j] = 0
                    if MatDirecciones[i][j] == 0:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i][j - 1] = 3
                        MatAuxHormigas[i][j - 1] = 1
                        j = j + 1
                    elif MatDirecciones[i][j] == 1:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i - 1][j] = 0
                        MatAuxHormigas[i - 1][j] = 1
                        j = j + 1
                    elif MatDirecciones[i][j] == 2:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i][j + 1] = 1
                        MatAuxHormigas[i][j + 1] = 1
                        j = j + 1 
                    elif MatDirecciones[i][j] == 3:
                        MatDirecciones[i][j] = 0
                        MatAuxDirecciones[i + 1][j] = 2
                        MatAuxHormigas[i + 1][j] = 1
                        j = j + 1
            else: 
                j = j + 1
        j = 0 
        i = i + 1          
    aux = aux + 1
    print(aux)
    MatHormigas = copy.deepcopy(MatAuxHormigas)    
    MatDirecciones = copy.deepcopy(MatAuxDirecciones)
    print(MatHormigas)   
    print(MatDirecciones)
    print(MatColores)
    MatAuxHormigas = copy.deepcopy(MatZeros)
    MatAuxDirecciones = copy.deepcopy(MatZeros)
    

    pygame.display.update()
    