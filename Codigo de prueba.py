import pygame, sys
from pygame.locals import *
from random import randint

NumCel = 5
MatAuxDirecciones = [[[0 for x in range(4)] for x in range(NumCel)] for y in range(NumCel)]
print(MatAuxDirecciones)

MatAuxDirecciones[3][4][0] = 1
MatAuxDirecciones[3][4][2] = 2

print(MatAuxDirecciones)