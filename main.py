
import pygame
from pygame.locals import *

from math import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#CRIANDO FORMA
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
'''
Para tranferir o círculo de lugar
x = R * cos (angle) + X_centre
y = R * sin(angle)  + Y_centre

posx, posy = 0, 0
sides = 32
radius = 1
'''
def circulo(posx, posy, sides, radius):
    glBegin(GL_LINES)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2d(cosine, sine)
    glEnd()

def parabola(posx, posy, sides, radius):
    glBegin(GL_LINES)
    for i in range(33):
        cosine = radius * cos(i * pi / sides) + posx
        sine = radius * sin(i * pi / sides) + posy
        glVertex2d(cosine, -sine)
    glEnd()

def parabola2(posx, posy, sides, radius):
    glBegin(GL_LINES)
    for i in range(33):
        cosine = radius * cos(i * pi / sides) + posx
        sine = radius * sin(i * pi / sides) + posy
        glVertex2d(cosine, sine)
    glEnd()

#CRIANDO JANELA DE VISUALIZAÇÃO
def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(40, display[0]/display[1], 1, 10)
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        circulo(0,0,64,1)
        parabola(0, 0.1 , 32, 0.5)
        circulo(0.5, -0.1, 64, 0.1)
        circulo(-0.5, -0.1, 64, 0.1)
        parabola2(0.25, 0.2, 32, 0.15)
        parabola2(-0.25, 0.2, 32, 0.15)
        pygame.display.flip()

main()