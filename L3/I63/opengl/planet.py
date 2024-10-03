#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

###############################################################
# variables globales importantes en programmation evenementiel car c'est l'utilisateur
# qui a le controle, en temps normal on évite les variables globales pour éviter les
# effets de bord.
year, day = 0, 0
quadric = None
# Couleurs RVBA
red = (1.0, 0.0, 1.0, 0.0)
yellow = (1.0, 1.0, 0.0, 0.0)
blue = (0.0, 0.0, 1.0, 0.0)
white = (1.0, 1.0, 1.0, 0.0)
zoom = 0
###############################################################
# 

def init():
    global quadric
    glClearColor (0.0, 0.0, 0.0, 0.0) # Couleur du fond, noir ici
    glShadeModel (GL_SMOOTH)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    glEnable(GL_DEPTH_TEST) # Active la profondeur
    glEnable(GL_LIGHTING) # Active l'eclairage, ne pas oublier le LIGHTi après 
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_DITHER)
    #light()

def light():
    global red, blue, white, yellow
    diffuse = (0.7, 0.7, 0.7, 1.0)
    specular = (0.001, 0.001, 0.001, 1.0)
    pos = (0, 0, 0.5, 1)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, yellow)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 9.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    #glLightfv(GL_LIGHT1, GL_POSITION, (0, 0, -10, 1))

    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)


def display():
    global red, blue, white, yellowGL_FRONT_AND_BACK
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Ne pas oublier le depth buffer
    #glColor4f (1.0, 1.0, 0.0, 1.0) # Que pour la 2D

    light_position = (0.0, 0.0, 2.2, 1.0)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, yellow)
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.2, 0.2, 0.0, 0.5))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, red)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 9.0)

    #glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glPushMatrix()
    glTranslate(0, 0, zoom)
    gluSphere(quadric, 1.0, 100, 16) # Soleil
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(2.0, 0.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, blue)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0,0,0,1))


    gluSphere(quadric, 0.2, 20, 8) # Terre
    glPopMatrix()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    #glMatrixMode(GL_PROJECTION)
    glMatrixMode(gluPerspective)

    glLoadIdentity()
    gluPerspective(20, 16/9, 50)
    # if width <= height:
    #     #glOrtho(-2.5, 2.5, -2.5*height/width, 2.5*height/width, -10.0, 10.0)
        
    # else:
    #     #glOrtho(-2.5*width/height, 2.5*width/height, -2.5, 2.5, -10.0, 10.0)
    #     gluPerspective(20, 16/9, 50)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, -15, 0, 0, 0, 0, 1, 0)

def keyboard(key, x, y):
    global day, year, zoom
    key = key.decode('utf-8')

    if key == 'j':
        day = (day + 10) % 360
    elif key == 'J':
        day = (day - 10) % 360
    elif key == 'a':
        year = (year + 5) % 360
    elif key == 'A':
        year = (year - 5) % 360
    elif key == '\033':
        # sys.exit( )  # Exception ignored
        glutLeaveMainLoop()
    elif key == 'z':
        zoom -= 0.1
    elif key == 's':
        zoom += 0.1

    
    glutPostRedisplay()  # indispensable en Python


def idle():
    """ Fonction qui sera appelée quand il n'y a pas d'action d'utilisateur"""
    global day, year
    day = (day + 10) % 360
    year = (year + 0.3) % 360
    glutPostRedisplay()
###############################################################
# MAIN


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

glutCreateWindow('planet')
glutReshapeWindow(512,512)

# Fonctions d'opengl qui prennent des callbacks
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutIdleFunc(idle)
init()

glutMainLoop()