
import pygame
from pygame.locals import *

from math import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

'''
Para tranferir o círculo de lugar
x = R * cos (angle) + X_centre
y = R * sin(angle)  + Y_centre

posx, posy = 0, 0
sides = 32
radius = 1
'''

#FUNÇÃO PARA CIRCULO MAIOR
def circulo(posx, posy, sides, radius):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2d(cosine, sine)
    glEnd()

#FUNÇÃO PARA SORRISO
def parabola(posx, posy, sides, radius):
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for i in range(33):
        cosine = radius * cos(i * pi / sides) + posx
        sine = radius * sin(i * pi / sides) + posy
        glVertex2d(cosine, -sine)
    glEnd()

#FUNÇÃO PARA OLHOS
def parabola2(posx, posy, sides, radius):
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for i in range(33):
        cosine = radius * cos(i * pi / sides) + posx
        sine = radius * sin(i * pi / sides) + posy
        #glLineWidth(5)
        glVertex2d(cosine, sine)
    glEnd()

#FUNÇÃO PARA BOCHECHAS
def circulo2(posx, posy, sides, radius):
    glColor3f(1.0, 0.0, 0.0) 
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2d(cosine, sine)
    glEnd()

def ponto(x, y):
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

#CRIANDO QUADRADO
vertices = ((1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1))
edge = ((0, 1), (1, 2), (2, 3), (3, 0))

def quadrado():
    glBegin(GL_LINES)
    for e in edge:
        for vertex in e:
            glVertex2iv(vertices[vertex])
    glEnd()