
import pygame
from pygame.locals import *

from math import *

import OpenGL
from OpenGL.GL import *
#from OpenGL.GLUT import *
from OpenGL.GLU import *

from formas import *

# DESENHO DO OBJETO


def drawEmoji():
    circulo(0, 0, 64, 1)
    parabola(0, 0.1, 32, 0.5)
    parabola2(0.25, 0.2, 32, 0.15)
    parabola2(-0.25, 0.2, 32, 0.15)
    circulo2(0.5, -0.1, 64, 0.1)
    circulo2(-0.5, -0.1, 64, 0.1)

# CRIANDO JANELA DE VISUALIZAÇÃO


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0]/display[1], 0.1, 50)
    glTranslate(0.0, 0.0, -5)
    # glScale(1.5, 1, 1) # TRANFORMAÇÃO ESCALA NO EIXO X DE 1.5*
    #glRotatef(90, 0, 0 , 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #AÇOES DE TRANSLAÇÃO COM BOTOES UP, DOWN, LEFT E RIGTH DO TECLADO    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslate(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslate(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslate(0,0.5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslate(0, -0.5, 0)

            #AÇOES DE ROTAÇÃO COM CLICK DO MOUSE  
            if event.type == pygame.MOUSEBUTTONDOWN:
                    #glRotatef(-90, 0, 0, 1.0)
                    glScalef(0.2,0.2,0.2)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #LIMPEZA CACHE

        #glTranslate(0, 0,-.10)
        #glRotatef(90, 0, 0 , 1.0)
        drawEmoji()
        pygame.display.flip()
        pygame.time.wait(20)


main()
