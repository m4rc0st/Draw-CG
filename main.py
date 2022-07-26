
import pygame
from pygame.locals import *

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
        quadrado()
        pygame.display.flip()

main()