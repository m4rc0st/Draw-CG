
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

    gluPerspective(65, display[0]/display[1], 0.1, 50)
    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #AÇOES DE TRANSLAÇÃO COM BOTOES LEFT E RIGTH DO TECLADO    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslate(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslate(0.5, 0, 0)

                #AÇOES DE ESCALA COM BOTOES UP E DOWN DO TECLADO
                if event.key == pygame.K_UP:
                    glScalef(1.1,1.1,1.1)
                if event.key == pygame.K_DOWN:
                    glScalef(0.8,0.8,0.8)

                #AÇOES DE REFLEXÃO NO EIXO COM BOTOES a, d DO TECLADOa
                if event.key == pygame.K_a:
                    glScalef(-1,1,1)
                if event.key == pygame.K_d:
                    glScalef(1,-1,1)

                #AÇOES DE REFLEXÃO NOS DOIS EIXO COM BOTAO s DO TECLADOa
                if event.key == pygame.K_s:
                    glScalef(-1,-1,1)
                     
            #AÇOES DE ROTAÇÃO COM CLICK DO MOUSE  
            if event.type == pygame.MOUSEBUTTONDOWN:
                    glRotatef(1.0, 0, -1.0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #LIMPEZA CACHE

        ponto(-1, -1) # ponto (-1,-1) para referência
        drawEmoji()
        pygame.display.flip()
        pygame.time.wait(20)


main()
