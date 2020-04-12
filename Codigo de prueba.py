import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()                           # A partir de esta linea funcionaran todas las instrucciones de pygame

DimTablero = 500
Ventana = pygame.display.set_mode((DimTablero,DimTablero))
pygame.display.set_caption('Programa de prueba')

azul = pygame.Color(50,50,200)
negro = pygame.Color(0,0,0)
blanco = pygame.Color(255,255,255)
Alto = 10
Ancho = 10
margen = 4


def Iterador(anch,marg,DimVent):
    i = 0
    n = 0
    a = anch + marg
    while n < DimVent:
        yield n
        i += 1
        n = i*a

#Dim = Iterador(Ancho,margen,DimVentana)    Usando esto arroja error ya que esto es una direccion de memoria en donde estan los valores del iterador
#print(*Dim)

#Dim = [0 ,25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
#print(Dim)

while True:                             # Loop infinito para mantener abierta la ventana
    for Evento in pygame.event.get():       # Se hara un recorrido a traves de los diferentes tipos de eventos que tiene la libreria
        if Evento.type == QUIT:
            pygame.quit()
            sys.exit
    for columna in Iterador(Ancho,margen,DimTablero):
        for fila in Iterador(Ancho,margen,DimTablero):
            pygame.draw.rect(Ventana,negro,(columna,fila,margen,Alto))
            pygame.draw.rect(Ventana,azul,(columna + margen,fila + margen, Ancho,Alto))
    pygame.display.update()
